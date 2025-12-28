from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Optional, Dict, Callable
import importlib
import pkgutil
import inspect
import functools
import textwrap

# --- Generated imports (no jellyfin_openapi name) ---
from ._generated.client import Client as UnauthClient
from ._generated.client import AuthenticatedClient

_DEFAULT = object()  # sentinel


def _codeblock(s: str) -> str:
    """Dedent + strip docstrings so help() output is clean."""
    return textwrap.dedent(s).strip()


def _default_emby_authorization(
    *,
    client_name: str,
    device: str,
    device_id: str,
    version: str,
) -> str:
    # Jellyfin expects this exact style for client identification.
    return (
        f'MediaBrowser Client="{client_name}", '
        f'Device="{device}", DeviceId="{device_id}", '
        f'Version="{version}"'
    )


@dataclass(frozen=True)
class JellyfinAuth:
    access_token: str
    user_id: str


class Jellyfin:
    """
    Dynamic facade over the generated OpenAPI client.

    This provides the following conviniences over using the raw generated
    openapi client:

     - Handles authentication with username / password
     - Put all generated endpoints under `.api.*`
     - Auto-injects ``client`` into generated calls when possible

    Design goals:
      - Keep manual surface small: login + client/auth properties
      - Avoid hardcoding endpoint wrappers; instead discover dynamically

    Usage:
        jf = Jellyfin(base_url=..., username=..., password=...)
        jf.login()  # optional if auto_login=True
        resp = jf.api.library.get_media_folders.sync_detailed()
    """
    DEFAULTS: Dict[str, Any] = {
        "client_name": "openapi-python-client",
        "device": "python",
        "device_id": "python-jellyfin",
        "version": "0.1.0",
        "timeout": 30.0,
        "auto_login": True,
        "mount_api": True,
        # Auth header defaults:
        "auth_header_name": "X-Emby-Token",
        "auth_prefix": "",
    }

    def __init__(
        self,
        *,
        base_url: str,
        username: str,
        password: str = "",
        client_name: Any = _DEFAULT,
        device: Any = _DEFAULT,
        device_id: Any = _DEFAULT,
        version: Any = _DEFAULT,
        timeout: Any = _DEFAULT,
        auto_login: Any = _DEFAULT,
        mount_api: Any = _DEFAULT,
        auth_header_name: Any = _DEFAULT,
        auth_prefix: Any = _DEFAULT,
        extra_headers: Optional[Dict[str, str]] = None,
    ):
        # Resolve defaults at runtime (no class-variable default trap)
        DEFAULTS = self.DEFAULTS
        client_name = DEFAULTS["client_name"] if client_name is _DEFAULT else client_name
        device = DEFAULTS["device"] if device is _DEFAULT else device
        device_id = DEFAULTS["device_id"] if device_id is _DEFAULT else device_id
        version = DEFAULTS["version"] if version is _DEFAULT else version
        timeout = DEFAULTS["timeout"] if timeout is _DEFAULT else timeout
        auto_login = DEFAULTS["auto_login"] if auto_login is _DEFAULT else auto_login
        mount_api = DEFAULTS["mount_api"] if mount_api is _DEFAULT else mount_api
        auth_header_name = DEFAULTS["auth_header_name"] if auth_header_name is _DEFAULT else auth_header_name
        auth_prefix = DEFAULTS["auth_prefix"] if auth_prefix is _DEFAULT else auth_prefix

        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password

        self._auto_login = bool(auto_login)
        self._timeout = float(timeout)

        self._auth_header_name = str(auth_header_name)
        self._auth_prefix = str(auth_prefix)

        # Jellyfin requires the identity header for lots of endpoints.
        self._identity_headers: Dict[str, str] = {
            "X-Emby-Authorization": _default_emby_authorization(
                client_name=str(client_name),
                device=str(device),
                device_id=str(device_id),
                version=str(version),
            )
        }
        if extra_headers:
            self._identity_headers.update(extra_headers)

        # Underlying generated clients
        self._unauth = UnauthClient(
            base_url=self.base_url,
            headers=self._identity_headers,
            timeout=self._timeout,
        )
        self._authed: Optional[AuthenticatedClient] = None
        self._auth: Optional[JellyfinAuth] = None

        # All generated endpoints live under .api
        parent_modpath = os.path.dirname(__file__)

        self.api = ApiNamespace(
            "api",
            doc=_codeblock(
                f"""
                Jellyfin API namespace (dynamically generated).

                This namespace contains endpoint groups created by crawling the generated
                OpenAPI client under `{parent_modpath}/_generated/api/*`.

                Usage
                -----
                jf.api.<group>.<endpoint>.sync(...)
                jf.api.<group>.<endpoint>.sync_detailed(...)
                jf.api.<group>.<endpoint>.asyncio(...)
                jf.api.<group>.<endpoint>.asyncio_detailed(...)

                Convenience behavior
                --------------------
                Endpoint proxies will auto-inject `client=jf.client` if you do not provide it.

                Introspection
                -------------
                dir(jf.api)                 -> list groups
                dir(jf.api.library)         -> list endpoints in the "library" group
                help(jf.api.library)        -> show info about an endpoint group
                help(jf.api.library.get_media_folders) -> show info about a specific endpoint
                """
            ),

        )
        if mount_api:
            self._mount_generated_api()

    # -------------------------
    # Auth / Client access
    # -------------------------

    @property
    def auth(self) -> JellyfinAuth:
        if self._auth is None:
            raise RuntimeError("Not logged in. Call jf.login() first.")
        return self._auth

    @property
    def user_id(self) -> str:
        return self.auth.user_id

    @property
    def client(self) -> AuthenticatedClient:
        # Lazy login if enabled
        if self._authed is None:
            if not self._auto_login:
                raise RuntimeError("Auto-login is disabled. Call jf.login() first.")
            self.login()
        if not self._authed:
            raise RuntimeError("Not logged in. Call jf.login() first.")
        return self._authed

    def login(self) -> JellyfinAuth:
        """
        Perform /Users/AuthenticateByName, store token/user_id, and construct AuthenticatedClient.

        This is the only method that needs to know about a specific endpoint.
        """
        # Generated login endpoint + model
        from ._generated.api.user import authenticate_user_by_name
        from ._generated.models import AuthenticateUserByName

        body = AuthenticateUserByName(username=self.username, pw=self.password)
        resp = authenticate_user_by_name.sync_detailed(client=self._unauth, body=body)

        if resp.status_code != 200 or resp.parsed is None:
            msg = resp.content.decode("utf-8", "ignore") if resp.content else ""
            raise RuntimeError(f"Login failed ({resp.status_code}): {msg}")

        parsed = resp.parsed

        token = getattr(parsed, "access_token", None) or getattr(parsed, "AccessToken", None)
        user = getattr(parsed, "user", None) or getattr(parsed, "User", None)
        user_id = getattr(user, "id", None) or getattr(user, "Id", None)

        if not token or not user_id:
            raise RuntimeError("Login response missing token or user id")

        self._auth = JellyfinAuth(access_token=token, user_id=user_id)

        # Jellyfin token header: typically X-Emby-Token, no "Bearer "
        self._authed = AuthenticatedClient(
            base_url=self.base_url,
            token=token,
            prefix=self._auth_prefix,
            auth_header_name=self._auth_header_name,
            headers=self._identity_headers,
            timeout=self._timeout,
        )

        return self._auth

    # -------------------------
    # Dynamic API mounting
    # -------------------------

    def _mount_generated_api(self) -> None:
        """
        Crawls ._generated.api.* and mounts endpoints under jf.api.<group>.<endpoint>.

        Each endpoint is wrapped in EndpointProxy so client= is auto-supplied when missing.
        """
        api_pkg_name = f"{__package__}._generated.api"
        api_pkg = importlib.import_module(api_pkg_name)

        # First-level packages under api/ become namespaces (user, library, system, etc.)
        for _, group_mod_name, group_is_pkg in pkgutil.iter_modules(api_pkg.__path__, api_pkg.__name__ + "."):
            if not group_is_pkg:
                continue

            group_mod = importlib.import_module(group_mod_name)
            group_name = group_mod_name.split(".")[-1]
            group_ns = ApiNamespace(
                group_name,
                doc=_codeblock(
                    f"""
                    Generated endpoint group: `{group_name}`

                    This namespace corresponds to modules under:

                        `_generated/api/{group_name}/`

                    Each attribute is an `EndpointProxy` wrapping a generated endpoint module.

                    Usage
                    -----
                        jf.api.{group_name}.<endpoint>.sync(...)
                        jf.api.{group_name}.<endpoint>.sync_detailed(...)

                    Introspection
                    -------------
                        dir(jf.api.{group_name}) -> list endpoints in this group
                        help(jf.api.{group_name}.<endpoint>) -> show proxy docs
                    """),
            )


            # Each .py file under that group is an endpoint module
            for _, endpoint_mod_name, endpoint_is_pkg in pkgutil.iter_modules(
                group_mod.__path__, group_mod.__name__ + "."
            ):
                if endpoint_is_pkg:
                    continue
                endpoint_mod = importlib.import_module(endpoint_mod_name)
                endpoint_name = endpoint_mod_name.split(".")[-1]

                # Wrap with proxy to auto-inject client=
                setattr(group_ns, endpoint_name, EndpointProxy(self, endpoint_mod))

            setattr(self.api, group_name, group_ns)

    def __repr__(self) -> str:
        return (
            f"<Jellyfin base_url={self.base_url!r} "
            f"user={self.username!r} authed={self._authed is not None}>"
        )



class ApiNamespace:
    """
    A simple object that holds dynamically attached endpoint proxies.
    The documentation will be overwritten for each instance.
    """
    def __init__(self, name: str, doc: str | None = None):
        self.__name__ = name
        self.__doc__ = doc or ""

    def __repr__(self) -> str:
        keys = [k for k in self.__dict__.keys() if not k.startswith("_")]
        keys.sort()
        preview = ", ".join(keys[:12]) + ("..." if len(keys) > 12 else "")
        return f"<ApiNamespace {self.__name__}: {preview}>"



class EndpointProxy:
    """
    Wraps a generated endpoint module and:
      - auto-populates client=... if missing
      - forwards .sync / .sync_detailed / .asyncio / .asyncio_detailed
      - still lets users access the raw module via ._module

    This keeps the generated surface intact but makes it more ergonomic.
    """

    def __init__(self, owner: "Jellyfin", module: Any):
        self._owner = owner
        self._module = module

        # Common generated entrypoints
        self.sync = self._wrap("sync")
        self.sync_detailed = self._wrap("sync_detailed")
        self.asyncio = self._wrap("asyncio")
        self.asyncio_detailed = self._wrap("asyncio_detailed")

        self.__doc__ = _codeblock(
            f"""
            EndpointProxy for generated endpoint module:

                {module.__name__}

            This object exposes (when available):

                - .sync(...)
                - .sync_detailed(...)
                - .asyncio(...)
                - .asyncio_detailed(...)

            Convenience behavior:

                If the underlying generated function accepts a `client=` parameter,
                the proxy will automatically populate it from `jf.client` when you do
                not supply one explicitly.

                This proxy is callable. Calling it is equivalent to calling `.sync_detailed(...)`:

                    jf.api.<group>.<endpoint>(...)  ==  jf.api.<group>.<endpoint>.sync_detailed(...)

            Introspection:

                - help(<this>.sync_detailed)  -> show signature + docstring
                - <this>._module              -> raw generated module
                - dir(<this>)                 -> list available call variants
            """)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """
        Default call behavior for an EndpointProxy.

        Equivalent to calling `.sync_detailed(...)`.

        Notes:
        - `client=` is auto-injected from `jf.client` if omitted.
        - Use `.sync(...)` if you want `parsed` directly (when available).
        """
        return self.sync_detailed(*args, **kwargs)


    def __repr__(self) -> str:
        return f"<EndpointProxy {self._module.__name__}>"

    def _wrap(self, fn_name: str) -> Callable[..., Any]:
        fn = getattr(self._module, fn_name, None)
        if fn is None:
            def _missing(*args: Any, **kwargs: Any) -> Any:
                raise AttributeError(f"{self._module.__name__} has no attribute {fn_name}")
            _missing.__doc__ = _codeblock(
                f"""
                Missing generated function:

                    {self._module.__name__}.{fn_name}

                This endpoint module does not provide the requested call variant.
                Typically this means you need to use the "asyncio_detailed" or
                "sync_detailed".
                """)
            return _missing

        try:
            orig_sig = inspect.signature(fn)
        except (TypeError, ValueError):
            orig_sig = None

        # If we can, create a "user-facing" signature that *omits* client
        user_sig = None
        if orig_sig is not None:
            params = list(orig_sig.parameters.values())
            params_wo_client = [p for p in params if p.name != "client"]
            user_sig = orig_sig.replace(parameters=params_wo_client)

        @functools.wraps(fn)
        def _call(*args: Any, **kwargs: Any) -> Any:
            # Autoinject client only if caller didn't provide it
            if "client" not in kwargs:
                if orig_sig is None or "client" in orig_sig.parameters:
                    kwargs["client"] = self._owner.client
            return fn(*args, **kwargs)

        # Make help() show the original (or filtered) signature
        if user_sig is not None:
            _call.__signature__ = user_sig  # type: ignore[attr-defined]
        elif orig_sig is not None:
            _call.__signature__ = orig_sig  # type: ignore[attr-defined]

        # Improve docstring: show that client is auto-injected + where to look
        # Overwrite docstring with: generated doc + proxy notes
        proxy_notes = _codeblock(f"""
            Notes
            -----
            This function is exposed through an `EndpointProxy` attached to the `Jellyfin`
            wrapper object.

            - If you do not supply `client=...`, it will be auto-populated from `jf.client`.
            - You can override this behavior by explicitly passing `client=...`.
            - Underlying generated function: `{self._module.__name__}.{fn_name}`

            Introspection
            -------------
            - help(jf.api.<group>.<endpoint>) shows proxy info
            - jf.api.<group>.<endpoint>._module is the raw generated endpoint module
            """)

        base_doc = (fn.__doc__ or "").rstrip()
        if base_doc:
            _call.__doc__ = base_doc + "\n\n" + proxy_notes
        else:
            _call.__doc__ = proxy_notes

        return _call


    def __getattr__(self, item: str) -> Any:
        # Forward any other attributes (rarely used but keeps things transparent).
        return getattr(self._module, item)
