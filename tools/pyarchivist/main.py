# -*- coding: UTF-8 -*-
from . import VERSION as _VER
from .Wikimedia_Commons import main as _wm_c_main
from argparse import ArgumentParser as _ArgParser
from functools import partial as _part
from sys import modules as _mods
from typing import Callable as _Call


def parser(parent: _Call[..., _ArgParser] | None = None):
    prog0 = _mods[__name__].__package__
    prog = prog0 if prog0 else __name__
    del prog0
    parser = (_ArgParser if parent is None else parent)(
        prog=f"python -m {prog}",
        description="archive data",
        add_help=True,
        allow_abbrev=False,
        exit_on_error=False,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{prog} v{_VER}",
        help="print version and exit",
    )
    subparsers = parser.add_subparsers(
        required=True,
    )
    _wm_c_main.parser(
        _part(subparsers.add_parser, _wm_c_main.__package__.replace(f"{prog}.", ""))
    )
    return parser
