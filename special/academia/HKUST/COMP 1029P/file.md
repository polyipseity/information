---
aliases:
  - Python file
  - Python files
tags:
  - flashcard/special/academia/HKUST/COMP_1029P/file
  - language/in/English
---

# Python file

## opening and closing

To open a file in reading mode, use {{`open(path, "r")` or `open(path)`}}. To open the file in writing mode, use {{`open(path, "w")`}}. <!--SR:!2024-04-21,60,310!2024-10-21,196,330-->

Always remember to {{close the file by calling `file.close()`}}. This is to ensure {{the file is unlocked or saved properly}}. A better method is using {{`with`}}, but it will not be mentioned here. <!--SR:!2024-12-26,254,330!2024-04-28,66,310!2024-04-27,65,310-->

Note that opening a nonexistent file {{will throw a `FileNotFoundError`. Furthermore, there are other possible errors that will throw an `IOError` or a subclass of it}}. So it is generally good to {{catch errors}} when opening files. <!--SR:!2024-04-24,64,310!2024-04-19,59,310-->

## reading

We can read the entire file into a string by {{calling `file.read()`}}. Alternatively, we can read the entire file into a list of lines by {{calling `file.readlines()`}}. <!--SR:!2024-04-24,63,310!2024-04-29,67,310-->

## writing

We can write string into a file by {{calling `file.write()`}}. Calling it multiple times {{concatenates the strings}}. <!--SR:!2024-11-07,213,330!2024-04-17,58,310-->
