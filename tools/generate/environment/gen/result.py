import typing as _typing
from .. import util as _util


@_typing.final
class Result:
    __slots__ = ('__location', '__text')

    def __init__(self: _typing.Self, *,
                 location: _util.Location,
                 text: str) -> None:
        self.__location: _util.Location = location
        self.__text: str = text

    def __repr__(self: _typing.Self) -> str:
        return f'{Result.__qualname__}(location={self.__location!r}, text={self.__text!r})'

    @property
    def location(self: _typing.Self) -> _util.Location: return self.__location

    @property
    def text(self: _typing.Self) -> str: return self.__text
