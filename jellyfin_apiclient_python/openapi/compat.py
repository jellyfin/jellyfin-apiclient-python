"""Runtime compatibility helpers for legacy Python versions.

These hooks allow the generated OpenAPI client to be imported on Python 3.8/3.9
without modifying the generated sources directly. Remove once those versions
are no longer supported.
"""
from __future__ import annotations

from pathlib import Path
import __future__
import importlib
import importlib.abc
import importlib.machinery
import sys
import textwrap
import typing

_GENERATED_PACKAGE = "jellyfin_apiclient_python.openapi._generated"


class _FutureAnnotationsLoader(importlib.machinery.SourceFileLoader):
    """Compile generated modules with postponed evaluation of annotations."""

    def get_source(self, fullname):
        source = super().get_source(fullname)
        if source and fullname == f"{_GENERATED_PACKAGE}.types" and sys.version_info < (3, 10):
            source = _rewrite_generated_types_source(source)
        if source and fullname.startswith(f"{_GENERATED_PACKAGE}.models") and sys.version_info < (3, 10):
            source = _rewrite_model_casts(source)
        return source

    def get_code(self, fullname):
        source = self.get_source(fullname)
        if source is None:
            return None
        return self.source_to_code(source, self.path)

    def source_to_code(self, data, path, *, _optimize=-1):
        return compile(
            data,
            path,
            "exec",
            flags=__future__.annotations.compiler_flag,  # type: ignore[name-defined]
            dont_inherit=True,
            optimize=_optimize,
        )


class _FutureAnnotationsFinder(importlib.abc.MetaPathFinder):
    """Wrap loaders for generated modules to avoid evaluating `|` at runtime on py3.8/3.9."""

    def find_spec(self, fullname: str, path: list[str] | None = None, target=None):
        if not fullname.startswith(_GENERATED_PACKAGE):
            return None
        spec = importlib.machinery.PathFinder.find_spec(fullname, path)
        if spec and isinstance(spec.loader, importlib.machinery.SourceFileLoader):
            spec.loader = _FutureAnnotationsLoader(fullname, spec.loader.path)  # type: ignore[attr-defined]
        return spec


def _install_future_annotations_importer() -> None:
    if any(isinstance(finder, _FutureAnnotationsFinder) for finder in sys.meta_path):
        return
    sys.meta_path.insert(0, _FutureAnnotationsFinder())


def _patch_typing_pep604() -> None:
    """Backport ``|`` support for typing aliases on Python <3.10."""

    def _as_union(lhs, rhs):
        return typing.Union[lhs, rhs]

    targets = [
        getattr(typing, "_GenericAlias", None),
        getattr(typing, "_SpecialGenericAlias", None),
    ]
    for target in targets:
        if target is None:
            continue
        try:
            target.__or__ = _as_union  # type: ignore[attr-defined]
            target.__ror__ = lambda self, other, _union=typing.Union: _union[other, self]  # type: ignore[attr-defined]
        except Exception:
            continue


def _rewrite_generated_types_source(source: str) -> str:
    """Rewrite union-heavy aliases to be Python 3.8/3.9 friendly without editing generated files."""

    replacement = """
# The types that `httpx.Client(files=)` can accept, copied from that library.
from typing import Union as _JF_Union, Tuple as _JF_Tuple, List as _JF_List, Optional as _JF_Optional, Mapping as _JF_Mapping

FileContent = _JF_Union[IO[bytes], bytes, str]
FileTypes = _JF_Union[
    _JF_Tuple[_JF_Optional[str], FileContent, _JF_Optional[str]],
    _JF_Tuple[_JF_Optional[str], FileContent, _JF_Optional[str], _JF_Mapping[str, str]],
]
RequestFiles = _JF_List[_JF_Tuple[str, FileTypes]]
"""

    return textwrap.dedent(replacement).strip()


def _rewrite_model_casts(source: str) -> str:
    """Avoid evaluating PEP604 unions inside typing.cast calls on older Python versions."""
    import re

    pattern = re.compile(r"cast\(([^,]*\|[^,]*),")
    return pattern.sub(lambda match: f'cast("{match.group(1).strip()}",', source)


def _ensure_patched_types_module() -> None:
    """Load a Python 3.8/3.9 compatible version of the generated types module."""
    if sys.version_info >= (3, 10):
        return
    name = f"{_GENERATED_PACKAGE}.types"

    path = Path(__file__).parent / "_generated" / "types.py"
    raw_source = path.read_text()

    marker = "# The types that `httpx.Client(files=)` can accept, copied from that library."
    try:
        start = raw_source.index(marker)
        end = raw_source.index("RequestFiles = list[tuple[str, FileTypes]]")
        end = raw_source.find("\n", end)
        remainder = raw_source[end + 1 :] if end != -1 else ""
        source = (
            raw_source[:start].rstrip("\n")
            + "\n"
            + _rewrite_generated_types_source("")
            + "\n"
            + remainder
        )
    except ValueError:
        source = _rewrite_generated_types_source(raw_source)

    if "| bytes | str" in source:
        raise RuntimeError("Failed to patch generated types module for Python < 3.10.")

    spec = importlib.util.spec_from_loader(name, loader=None, origin=str(path))
    module = importlib.util.module_from_spec(spec)
    exec(
        compile(source, str(path), "exec", flags=__future__.annotations.compiler_flag, dont_inherit=True),
        module.__dict__,
    )
    sys.modules[name] = module


def install_legacy_openapi_compat() -> None:
    """Install import hooks and type patches for legacy Python."""
    _patch_typing_pep604()
    _install_future_annotations_importer()
    _ensure_patched_types_module()


__all__ = ["install_legacy_openapi_compat"]
