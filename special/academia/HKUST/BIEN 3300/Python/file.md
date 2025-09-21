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

To open a file in reading mode, use {@{`open(path, "r")` or `open(path)`}@}. To open the file in writing mode, use {@{`open(path, "w")`}@}. <!--SR:!2025-09-25,4,270!2025-09-25,4,270-->

Always remember to {@{close the file by calling `file.close()`}@}. This is to ensure {@{the file is unlocked or saved properly}@}. A better method is using {@{`with`}@}, but it will not be mentioned here. <!--SR:!2025-09-25,4,270!2025-09-25,4,270!2025-09-25,4,270-->

Note that {@{opening a nonexistent file}@} will {@{throw a `FileNotFoundError`}@}. Furthermore, there are {@{other possible errors that will throw an `IOError` or a subclass of it}@}. So it is generally good to {@{catch errors}@} when opening files. <!--SR:!2025-09-25,4,270!2025-09-25,4,270!2025-09-26,4,282!2025-09-26,4,282-->

## reading

We can read the entire file into a string by {@{calling `file.read()`}@}. Alternatively, we can read the entire file into a list of lines by {@{calling `file.readlines()`}@}. <!--SR:!2025-09-25,4,270!2025-09-25,4,270-->

## writing

We can write string into a file by {@{calling `file.write()`}@}. Calling it multiple times {@{concatenates the strings}@}. <!--SR:!2025-09-25,4,270!2025-09-25,4,270-->
