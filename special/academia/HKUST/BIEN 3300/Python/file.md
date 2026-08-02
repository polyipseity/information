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

To open a file in reading mode, use {@{`open(path, "r")` or `open(path)`}@}. To open the file in writing mode, use {@{`open(path, "w")`}@}. <!--SR:!2026-10-27,290,330!2026-09-30,263,330-->

Always remember to {@{close the file by calling `file.close()`}@}. This is to ensure {@{the file is unlocked or saved properly}@}. A better method is using {@{`with`}@}, but it will not be mentioned here. <!--SR:!fsrs,2029-06-30T00:00:00.000Z,1053,1053.01305103,1,2,9,0,0,2026-08-12T00:00:00.000Z!2026-08-30,252,330!2026-10-05,268,330-->

Note that {@{opening a nonexistent file}@} will {@{throw a `FileNotFoundError`}@}. Furthermore, there are {@{other possible errors that will throw an `IOError` or a subclass of it}@}. So it is generally good to {@{catch errors}@} when opening files. <!--SR:!fsrs,2029-07-21T00:00:00.000Z,1068,1068.495917,1,2,9,0,0,2026-08-18T00:00:00.000Z!2026-10-13,276,330!2026-11-13,307,342!2026-11-12,306,342-->

## reading

We can read the entire file into a string by {@{calling `file.read()`}@}. Alternatively, we can read the entire file into a list of lines by {@{calling `file.readlines()`}@}. <!--SR:!2026-10-29,292,330!fsrs,2029-08-04T00:00:00.000Z,1080,1080.08717202,1,2,9,0,0,2026-08-20T00:00:00.000Z-->

## writing

We can write string into a file by {@{calling `file.write()`}@}. Calling it multiple times {@{concatenates the strings}@}. <!--SR:!2026-09-25,258,330!2026-10-08,271,330-->
