import typing as _typing

from ... import globals as _globals
from . import util as _util


@_typing.overload
def read_flashcard_states(text: str) -> _typing.Iterator[str]: ...
@_typing.overload
def read_flashcard_states(text: _util.Location) -> _typing.Iterator[str]: ...


def read_flashcard_states(text: str | _util.Location | _typing.Any) -> _typing.Iterator[str]:
    text0: str
    if isinstance(text, str):
        text0 = text
    elif isinstance(text, _util.Location):
        io: _typing.TextIO
        with text.open() as io:
            text0 = io.read()
    else:
        raise TypeError(text)

    return (found[0] for found in _globals.flashcard_regex.finditer(text0))
