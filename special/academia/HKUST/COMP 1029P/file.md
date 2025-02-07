---
aliases:
  - Python file
  - Python files
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029P/file
  - language/in/English
---

# Python file

## opening and closing

To open a file in reading mode, use {@{`open(path, "r")` or `open(path)`}@}. To open the file in writing mode, use {@{`open(path, "w")`}@}. <!--SR:!2028-02-03,1133,350!2027-04-04,895,350-->

Always remember to {@{close the file by calling `file.close()`}@}. This is to ensure {@{the file is unlocked or saved properly}@}. A better method is using {@{`with`}@}, but it will not be mentioned here. <!--SR:!2028-02-25,1156,350!2028-08-27,1297,350!2028-07-19,1265,350-->

Note that opening a nonexistent file {@{will throw a `FileNotFoundError`. Furthermore, there are other possible errors that will throw an `IOError` or a subclass of it}@}. So it is generally good to {@{catch errors}@} when opening files. <!--SR:!2026-07-24,621,310!2027-12-29,1107,350-->

## reading

We can read the entire file into a string by {@{calling `file.read()`}@}. Alternatively, we can read the entire file into a list of lines by {@{calling `file.readlines()`}@}. <!--SR:!2028-05-15,1215,350!2027-04-02,866,330-->

## writing

We can write string into a file by {@{calling `file.write()`}@}. Calling it multiple times {@{concatenates the strings}@}. <!--SR:!2027-07-04,969,350!2026-11-14,758,330-->
