import logging as _logging
import os as _os
import pathlib as _pathlib
import sys as _sys
import types as _types
import typing as _typing
import inspect as _inspect

_root_dir_excludes: _typing.AbstractSet[str] = frozenset(
    {'.git', '.obsidian', 'templates', 'tools', })


def main() -> None:
    argv: _typing.Sequence[str] = tuple(_sys.argv)
    try:
        frame: _types.FrameType | None = _inspect.currentframe()
        if frame is None:
            raise ValueError(frame)
        filename: str = _inspect.getframeinfo(frame).filename
        folder: _pathlib.Path = _pathlib.Path(
            filename).parent.resolve(strict=True)
        import tools.generate.main

        def generate_args0() -> _typing.Iterator[str]:
            root: str
            dirs: _typing.MutableSequence[str]
            files: _typing.Sequence[str]
            for root, dirs, files in _os.walk(folder):
                if _pathlib.Path(root).resolve(strict=True) == folder:
                    exclude: str
                    for exclude in _root_dir_excludes:
                        try:
                            dirs.remove(exclude)
                        except ValueError:
                            pass
                file: str
                for file in files:
                    if file.endswith('.md'):
                        yield _os.path.join(root, file)
        generate_args: _typing.Sequence[str] = tuple(generate_args0())
        print(f'Generating text from {len(generate_args)} input(s)')
        tools.generate.main.main(argv + generate_args)
    except Exception:
        _logging.exception('Uncaught exception')
    finally:
        print('Press <enter> to exit')
        input()


if __name__ == '__main__':
    main()
