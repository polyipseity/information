from glob import glob
from path import Path
from subprocess import run
from sys import executable


def main():
    files = glob("**/*.html", recursive=True)
    for file in files:
        if not file.endswith("Zinc.html"):
            continue
        file = Path(file)
        data = run(
            (executable, "tools/convert HKUST Zinc submission.py"),
            capture_output=True,
            text=True,
            input=f"{file}\r\n",
        )
        if data.returncode:
            print(f"Failed: {file}")
            continue
        submission = file.with_name("submission.yml")
        counter = 0
        while submission.exists():
            counter += 1
            submission = submission.with_name(f"submission ({counter}).yml")
        submission.write_bytes(data.stderr.encode())
        file.remove()


if __name__ == "__main__":
    main()
