import appdirs as _appdirs
import inspect as _inspect
import json as _json
import logging as _logging
import os as _os
import pathlib as _pathlib
import sys as _sys
import types as _types
import typing as _typing

_root_dir_excludes: _typing.AbstractSet[str] = frozenset(
    {'.git', '.obsidian', 'templates', 'tools', })
_local_app_dirs: _appdirs.AppDirs = _appdirs.AppDirs(
    appname='9a27fc39-496b-4b4c-87a7-03b9e88fc6bc',
    appauthor='polyipseity',
    version=None,
    roaming=False,
    multipath=False,
)


def main() -> None:
    argv: _typing.Sequence[str] = tuple(_sys.argv)
    try:
        frame: _types.FrameType | None = _inspect.currentframe()
        if frame is None:
            raise ValueError(frame)
        filename: str = _inspect.getframeinfo(frame).filename
        folder: _pathlib.Path = _pathlib.Path(
            filename).parent.resolve(strict=True)
        local_data_folder: _pathlib.Path = _pathlib.Path(
            _local_app_dirs.user_data_dir)
        local_data_folder.mkdir(parents=True, exist_ok=True)
        local_data_folder = local_data_folder.resolve(strict=True)

        import tools.generate.main
        generate_data_path: _pathlib.Path = local_data_folder / 'generate.json'
        if not generate_data_path.exists():
            generate_data_path.write_text('')
        generate_data: _typing.TextIO
        with open(generate_data_path, mode='r+t', encoding='UTF-8', errors='strict', newline=None,) as generate_data:
            try:
                data: _typing.MutableMapping[str, _typing.Any] = _json.load(
                    generate_data)
            except _json.decoder.JSONDecodeError:
                data = {}
                print('Generate data is empty or corrupted so it will be regenerated')
            finalizers: _typing.MutableSequence[_typing.Callable[[], None]] = [
            ]

            def generate_args0() -> _typing.Iterator[str]:
                mod_times: _typing.MutableMapping[str, int] = data.setdefault(
                    'mod_times', {})

                def on_error(err: OSError) -> None:
                    try:
                        raise err
                    except OSError:
                        _logging.exception('Exception while walking folders')
                root: str
                dirs: _typing.MutableSequence[str]
                files: _typing.Sequence[str]
                for root, dirs, files in _os.walk(folder, topdown=True, onerror=on_error, followlinks=False):
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
                            ret: str = _os.path.join(root, file)
                            try:
                                if mod_times[ret] != _os.lstat(ret).st_mtime_ns:
                                    yield ret
                            except KeyError:
                                yield ret

                            def update(mod_times: _typing.MutableMapping[str, int] = mod_times, ret: str = ret):
                                mod_times[ret] = _os.lstat(ret).st_mtime_ns
                            finalizers.append(update)
                mod_times.clear()
            generate_args: _typing.Sequence[str] = tuple(generate_args0())
            print(f'Generating text from {len(generate_args)} input(s)')
            if generate_args:
                tools.generate.main.main(argv + generate_args)

            finalizer: _typing.Callable[[], None]
            for finalizer in finalizers:
                finalizer()
            generate_data.seek(0)
            _json.dump(data, generate_data,
                       ensure_ascii=False, sort_keys=True, indent=2)
            generate_data.truncate()
    except Exception:
        _logging.exception('Uncaught exception')
    finally:
        print('Press <enter> to exit')
        input()


if __name__ == '__main__':
    main()
