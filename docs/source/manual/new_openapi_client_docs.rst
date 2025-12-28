Jellyfin OpenAPI Python Client
==============================

There are two ways to use it:

1. **Use the generated client directly** (lowest magic, most explicit).
2. **Use the convenience wrapper** (easy login + dynamic endpoint access).

Both approaches use the same generated code and models.

Using the Convenience Wrapper (Recommended)
-------------------------------------------

The ``jellyfin_apiclient_python.openapi.Jellyfin`` class provides:

- A simple ``login()`` method
- A lazily-created authenticated client (``jf.client``)
- A dynamically generated API namespace (``jf.api``)
- Automatic injection of ``client=jf.client`` into endpoint calls when omitted

Create a client and login
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from jellyfin_apiclient_python.openapi.client import Jellyfin

   jf = Jellyfin(
       base_url="http://127.0.1.1:8096",
       username="your-username",
       password="your-password",
   )

   # Explicit login (optional if auto_login=True)
   jf.login()

   print("UserId:", jf.user_id)

Call any generated endpoint dynamically
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All generated endpoints are mounted under ``jf.api`` as:

::

   jf.api.<group>.<endpoint>

For example:

.. code-block:: python

   # "system" group
   ping = jf.api.system.get_ping_system()
   print(ping.status_code)

   # "user_library" and "items" group
   root_resp = jf.api.user_library.get_root_folder(user_id=jf.user_id)
   item_resp = jf.api.items.get_items(parent_id=root_resp.parsed.id)

   items = item_resp.parsed.items
   for item in items:
       print(item.name, item.id)

Note that in these calls we did not pass ``client=...``. The proxy layer will
auto-populate ``client=jf.client`` when the underlying generated function
accepts a ``client`` argument.

Introspection (REPL friendly)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The dynamic API is designed to be discoverable:

.. code-block:: python

   dir(jf.api)               # list groups (user, items, library, system, ...)
   dir(jf.api.items)       # list endpoints in that group
   help(jf.api.items)      # describes the namespace
   help(jf.api.items.get_items)  # describes the endpoint proxy
   help(jf.api.items.get_items.sync_detailed)  # shows signature + docs



Using the Generated Client Directly (No Convenience Layer)
----------------------------------------------------------

If you prefer explicit control, you can use the generated client directly.

The Jellyfin server expects *two* authentication-related headers that you must provide:

1. A client identity header: ``X-Emby-Authorization``
2. An API token header: typically ``X-Emby-Token`` (no ``Bearer`` prefix)

You must also manually import the endpoints you wish to use and provide the client as an argument.

Step 1: Create the identity header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   BASE_URL = "http://127.0.1.1:8096"
   username = 'your-username'
   password = 'your-password'

   headers = {
       "X-Emby-Authorization": (
           'MediaBrowser Client="openapi-python-client", '
           'Device="python", DeviceId="python-jellyfin-test", '
           'Version="0.0.0"'
       )
   }

Step 2: Login to obtain an API token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from jellyfin_apiclient_python.openapi._generated.client import Client
   from jellyfin_apiclient_python.openapi._generated.api.user import authenticate_user_by_name
   from jellyfin_apiclient_python.openapi._generated.models import AuthenticateUserByName

   client = Client(base_url=BASE_URL, headers=headers)

   resp = authenticate_user_by_name.sync_detailed(
       client=client,
       body=AuthenticateUserByName(username=username, pw=password),
   )

   assert resp.status_code == 200
   auth = resp.parsed
   token = auth.access_token
   user_id = auth.user.id

Step 3: Use ``AuthenticatedClient`` for subsequent requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Jellyfin expects the token to be sent using ``X-Emby-Token`` with *no* prefix.

.. code-block:: python

   from jellyfin_apiclient_python.openapi._generated.client import AuthenticatedClient

   authed = AuthenticatedClient(
       base_url=BASE_URL,
       token=token,
       prefix="",                 # IMPORTANT: no "Bearer "
       auth_header_name="X-Emby-Token",
       headers=headers,           # keep identity header too
   )

Now call any endpoint:

.. code-block:: python

    from jellyfin_apiclient_python.openapi._generated.api.user_library import get_root_folder
    from jellyfin_apiclient_python.openapi._generated.api.items import get_items

    root_resp = get_root_folder.sync_detailed(client=authed, user_id=user_id)

    item_resp = get_items.sync_detailed(client=authed, parent_id=root_resp.parsed.id)
    items = item_resp.parsed.items
    for item in items:
        print(item.name, item.id)
