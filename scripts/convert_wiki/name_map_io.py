"""Load, merge, and persist the Wikipedia title rename map."""

import json
from collections.abc import Mapping
from contextlib import suppress
from os import PathLike

from anyio import Path

from . import config as _cfg

"""Exported names from this module."""
__all__ = ()


def _merge_names_maps(*maps: Mapping[str, str]) -> dict[str, str]:
    """Merge name maps left-to-right; later entries override earlier ones."""
    merged: dict[str, str] = {}
    for names_map in maps:
        merged.update(names_map)
    return merged


def _new_mapping_keys(
    base: Mapping[str, str],
    effective: Mapping[str, str],
) -> tuple[str, ...]:
    """Return keys added or changed between *base* and *effective*."""
    return tuple(
        key for key, value in effective.items() if key not in base or base[key] != value
    )


async def _save_names_map(
    names_map: Mapping[str, str],
    *,
    path: PathLike[str] | None = None,
) -> None:
    """Atomically persist the name map as sorted JSONC-compatible JSON."""
    resolved_path = Path(
        path
        if path is not None
        else _cfg._DATA_DIRECTORY / f"{_cfg._NAMES_MAP_NAME}.name_map.jsonc"
    )
    tmp = resolved_path.with_suffix(".tmp")
    payload = json.dumps(dict(names_map), ensure_ascii=False, indent=2, sort_keys=True)
    try:
        await tmp.write_text(f"{payload}\n", encoding="UTF-8")
        await tmp.replace(resolved_path)
    except BaseException:
        with suppress(FileNotFoundError):
            await tmp.unlink()
        raise


def _reload_names_map() -> None:
    """Reload the module-level name map from disk."""
    _cfg._NAMES_MAP = _cfg._load_names_map()
