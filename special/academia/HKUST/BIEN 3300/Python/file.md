---
aliases:
  - Python file
  - Python files
tags:
  - flashcard/active/special/academia/HKUST/BIEN_3300/Python/file
  - language/in/English
---

# Python file

## opening and closing

To open a file in reading mode, use {@{`open(path, "r")` or `open(path)`}@}. To open the file in writing mode, use {@{`open(path, "w")`}@}. <!--SR:!2025-12-31,66,310!2025-12-24,60,310-->

Always remember to {@{close the file by calling `file.close()`}@}. This is to ensure {@{the file is unlocked or saved properly}@}. A better method is using {@{`with`}@}, but it will not be mentioned here. <!--SR:!2026-08-11,236,330!2025-12-21,58,310!2025-12-25,61,310-->

Note that {@{opening a nonexistent file}@} will {@{throw a `FileNotFoundError`}@}. Furthermore, there are {@{other possible errors that will throw an `IOError` or a subclass of it}@}. So it is generally good to {@{catch errors}@} when opening files. <!--SR:!2025-12-20,57,310!2025-12-29,64,310!2026-01-02,68,322!2026-01-03,68,322-->

## reading

We can read the entire file into a string by {@{calling `file.read()`}@}. Alternatively, we can read the entire file into a list of lines by {@{calling `file.readlines()`}@}. <!--SR:!2026-01-01,67,310!2026-08-19,243,330-->

## writing

We can write string into a file by {@{calling `file.write()`}@}. Calling it multiple times {@{concatenates the strings}@}. <!--SR:!2025-12-23,59,310!2025-12-26,62,310-->
