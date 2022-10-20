import logging as _logging
import os as _os
import pathlib as _pathlib
import sys as _sys
import types as _types
import typing as _typing
import inspect as _inspect


def main() -> None:
    argv: _typing.Sequence[str] = tuple(_sys.argv)
    try:
        frame: _types.FrameType | None = _inspect.currentframe()
        if not frame:
            raise ValueError(frame)
        filename: str = _inspect.getframeinfo(frame).filename
        folder: _pathlib.PurePath = _pathlib.PurePath(filename).parent
        import tools

        def generate_args0() -> _typing.Iterator[str]:
            root: str
            files: _typing.Sequence[str]
            for root, _, files in _os.walk(folder):
                file: str
                for file in files:
                    if file.endswith('.md'):
                        yield _os.path.join(root, file)
        generate_args: _typing.Sequence[str] = tuple(generate_args0())
        print(f'Generating text from {len(generate_args)} input(s)')
        tools.generate.main.main(argv + generate_args)
    except:
        _logging.exception('Uncaught exception')
    finally:
        input('Press <enter> to exit')


if __name__ == '__main__':
    main()
