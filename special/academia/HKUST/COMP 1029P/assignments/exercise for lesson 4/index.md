---
aliases:
  - HKUST COMP 1029P exercise for lesson 4
tags:
  - date/2024/01/22
  - language/in/English
---

# exercise for lesson 4

- HKUST COMP 1029P

<!-- list separator -->

- due: 2024-01-22T23:59:59+08:00
- points: 100
- submitting: a file upload
- file types: py
- available: until 2024-01-22T23:59:59+08:00

## __A Phone Book Database__

## Introduction

For this exercise, you will write a small set of utilities by writing three functions:

- `db_create()` - for creating a text database
- `db_add()` - for adding records to a text database. This function is given to you.
- `db_query()` - for retrieving information from a text database and handles user's query

These 3 functions are started by a main menu inside the Python program.

## The Main Menu

Here is the main menu shown by running the program:

Welcome to the phone book database system!

```console
Welcome to the phone book database system!

Please select from one of the following:

  c - Create a new phone book database
  a - Add a new entry to an existing phone book database
  q - Make queries from an existing phone book database

  x - Exit the system

(c/a/q/x):
```

By entering 'c', 'a', 'q' or 'x', you will be able to use the 3 functions and exit the system respectively. For example, if you enter 'x', the program will finish:

```console
Welcome to the phone book database system!
...
(c/a/q/x):  x
Bye!
```

If you enter 'c', the program will run `db_create()`. If you enter 'a', the program will run `db_add()` and if you enter 'q', the program will run `db_query()`.

## Examples of the Three Functions

Here is an example of using the 3 functions.

```console
Welcome to the phone book database system!
...
(c/a/q/x):  c
Enter the filename of the new database: myfriends
Enter a name: David
Enter a phone number: 1234 5678
Enter a name: Sarah
Enter a phone number: 9876 5432
Enter a name: done
Done.

Welcome to the phone book database system!
...
(c/a/q/x):  a
Enter the filename of the database: blah
There is no file by that name. Try again...
Enter the filename of the database: myfriends
Enter a name: Esther
Enter a phone number: 8888 8888
Enter a name: done
Done.

Welcome to the phone book database system!
...
(c/a/q/x):  q
Enter the filename of the database: myfriends
Enter a name: Sarah
9876 5432
Enter a name: Esther
8888 8888
Enter a name: Edward
Sorry, there is no number for that name
Enter a name: done
Done.

Welcome to the phone book database system!
...
(c/a/q/x): x
Bye!
```

## Part 1 - Database Creation

Write a function called `db_create()` that takes no inputs and behaves as follows:

- The user is asked for the filename of the database to write.
- Then, the user is repeatedly asked to enter a name, and then a phone number. Alternatively, the user can enter the string `"done"` and the function prints `"Done."` and ends. The names and phone numbers are then stored in the file.

### Example Sequence

Here is example of using the function:

```console
Enter the filename of the new database: myfriends
Enter a name: David
Enter a phone number: 1234 5678
Enter a name: Sarah
Enter a phone number: 9876 5432
Enter a name: done
Done.
```

## Part 2 - Database Addition

Write a function called `db_add()` that takes no inputs and behaves as follows:

- The user is asked for the filename of an existing database file.
- If no file with that name exists, an exception is caught using `try-except` and the user is asked to enter a new file name.
- When a valid file name is given, the user is repeatedly queried to add a new name and phone number until the user enters `"done"` and the function prints `"Done."` and ends. These new entries are saved in the file.

The function `db_add()` is given to you and you should not change it.

<!-- markdownlint-disable-next-line MD024 -->
### Example Sequence

Here is an example of using the function:

```console
Enter the filename of the database: blah
There is no file by that name. Try again...
Enter the filename of the database: myfriends
Enter a name: Esther
Enter a phone number: 8888 8888
Enter a name: done
Done.
```

## Part 3 - Database Queries

Write a function called `db_query()` that takes no inputs and works like this:

- The user is asked for the filename of an existing database.
- If no file with that name exists, an exception is caught using `try-except` and the user is asked to enter a new file name.
- When a valid file name is given, the function loads the names and phone numbers from the file into a Python ___dictionary___ where the keys are the names and the values are the phone numbers.
- Then, the program goes into a loop where the user is asked for a name and the program prints the phone number.
  - If the user types `"done"` for the name, the program prints `"Done."` and ends.
  - If the user types a name that is not in the database and not `"done"`, then a friendly error message is displayed, such as `"Sorry, there is no number for that name."`

Notice that `db_create()` and `db_add()` can create duplicated entries \(entries which use the same name\) in the database. Because you will use a dictionary in `db_query()` if you ask for a name with more than one entry in the database `db_query()` will return only one of the phone numbers. This is fine for the exercise but in the real world, when the user wants to add an entry with the same name the database should warn the user the name has been stored in the database.

<!-- markdownlint-disable-next-line MD024 -->
### Example Sequence

Here is an example of using the function:

```console
Enter the filename of the database: myfriends
Enter a name: Sarah
9876 5432
Enter a name: Esther
8888 8888
Enter a name: Edward
Sorry, there is no number for that name
Enter a name: done
Done.
```

## Starting Code

You may download the code below as your starting code:

[phonebook.py](template/phonebook.py)

## Testing Your Functions

You should test your `db_create()` function first before testing the other two. Once you have done that, you can examine the content of the text file created by your function. Apart from using `db_add()` to adjust the content of the phone book, you can also freely change the text file given you follow the "two lines entry" format.

Assuming you don't have the file `myfriends` created before, if you use the functions in the shell like in the example sequence shown above, it should show exactly the same output.

## Submission

You need to complete the 2 functions in a file called ___phonebook.py___.

In your phonebook.py, include these:

- the function `db_create()`, which creates a text database. You need to complete this function.
- the function `db_add()`, which adds more records to an existing text database. This function is given to you. You do not need to change it.
- the function `db_query()`, which retrieves information from a text database and handles user's query. You need to complete this function.

After you have finished your work, upload your file and then submit by clicking the "Submit Assignment", and then choosing your file to submit.

## submission

- file: [phonebook.py](submission/phonebook.py)
