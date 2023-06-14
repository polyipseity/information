# -*- coding: UTF-8 -*-
from distutils.version import StrictVersion as _SVer
from logging import INFO as _INFO, basicConfig as _basicConfig, getLogger as _getLogger
from sys import version as _ver
from typing import Literal as _Lit, TypedDict as _TDict, final as _fin


@_fin
class _OpenOptions(_TDict):
    encoding: str
    errors: _Lit[
        "strict",
        "ignore",
        "replace",
        "surrogateescape",
        "xmlcharrefreplace",
        "backslashreplace",
        "namereplace",
    ]
    newline: None | _Lit["", "\n", "\r", "\r\n"]


# update `pyproject.toml`
AUTHORS = [
    {
        "name": "William So",
        "email": "polyipseity@gmail.com",
    }
]
NAME = "pyarchivist"
VERSION = _SVer("1.0.0")

_basicConfig(level=_INFO)
LOGGER = _getLogger(NAME)
OPEN_TEXT_OPTIONS: _OpenOptions = {
    "encoding": "UTF-8",
    "errors": "strict",
    "newline": None,
}
USER_AGENT = f"{NAME}/{VERSION} ({AUTHORS[0]['email']}) Python/{_ver}"
