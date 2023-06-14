# -*- coding: UTF-8 -*-
from .main import parser as _parser
from asyncio import run as _run
from sys import argv as _argv

if __name__ == "__main__":
    entry = _parser().parse_args(_argv[1:])
    _run(entry.invoke(entry))
