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

To open a file in reading mode, use {{`open(path, "r")` or `open(path)`}}. To open the file in writing mode, use {{`open(path, "w")`}}. <!--SR:!2024-02-21,16,290!2024-04-06,48,310-->

Always remember to {{close the file by calling `file.close()`}}. This is to ensure {{the file is unlocked or saved properly}}. A better method is using {{`with`}}, but it will not be mentioned here. <!--SR:!2024-04-16,57,310!2024-02-22,17,290!2024-02-22,17,290-->

Note that opening a nonexistent file {{will throw a `FileNotFoundError`. Furthermore, there are other possible errors that will throw an `IOError` or a subclass of it}}. So it is generally good to {{catch errors}} when opening files. <!--SR:!2024-04-24,64,310!2024-04-19,59,310-->

## reading

We can read the entire file into a string by {{calling `file.read()`}}. Alternatively, we can read the entire file into a list of lines by {{calling `file.readlines()`}}. <!--SR:!2024-02-21,16,290!2024-02-22,17,290-->

## writing

We can write string into a file by {{calling `file.write()`}}. Calling it multiple times {{concatenates the strings}}. <!--SR:!2024-04-07,49,310!2024-04-17,58,310-->
