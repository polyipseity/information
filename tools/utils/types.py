import\
    os as _os,\
    typing as _typing

Path: _typing.TypeAlias = str | _os.PathLike[str] | bytes | _os.PathLike[bytes]
