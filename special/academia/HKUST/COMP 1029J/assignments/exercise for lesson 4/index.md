---
aliases:
  - HKUST COMP 1029J exercise for lesson 4
tags:
  - date/2024/01/22
  - language/in/English
---

# exercise for lesson 4

- HKUST COMP 1029J

---

- title: Exercise for Lesson 4
- due: 2024-01-22T23:59:59+08:00
- points: 100
- submitting: a file upload
- file types: java
- available: until 2024-01-22T23:59:59+08:00

---

## __A Phone Book Program__

## Introduction

```console
Welcome to the phone book program.

Please choose one of the following:

1) Add New Phone Number
2) List Phone Numbers
3) Find Phone Number by Name
4) Delete Phone Number by Name
5) Quit

Please enter 1, 2, 3, 4 or 5:
```

Earlier in this lesson we have discussed a simple phone book program using a text file to store phone number entries. In this exercise you are going to improve the phone book program by adding a few additional features.

Recall that the simple phone book program allows you to do only two things:

- Add a new phone number
- List current phone numbers

Now we want the phone book program to be extended so that it has the following additional features:

- Do not allow duplicated entries in the phone book
- Find a phone number entry by name
- Delete a phone number entry by name

In this exercise you need to complete these additional features one by one for the extended phone book program. Here are the tasks in the exercise:

1. Checking for duplicated entry when a new phone number is added
2. Finding a phone number entry by name
3. Delete a phone number entry by name

## Overview

Here is the code of the program:

[PhoneBookEntry.java](template/PhoneBookEntry.java.md)

and [PhoneBook.java](template/PhoneBook.java)

### The Data File

You can get the initial data file from here: [phonebook.txt](template/phonebook.txt)

The format of the data file __phonebook.txt__ is slightly different to the one used by the simple phone book program given in the lesson.

In this exercise, each phone number entry is still stored as a separate line. However, the name and the phone number of one entry are separated by a colon, without a space. You can see the format of the phone book from the given __phonebook.txt__, as shown below:

```text
CSO:2358-6333
FMO:2358-6421
FO:2358-6418
HRO:2358-6580
ITSC:2358-6188
SAO:2358-0842
```

### Adding a New Phone Number

The phone book program allows you to add a phone number to the phone book. However, you cannot add two entries of the same name. Here is what you see when you want to add a new phone number using an existing name:

```console
Welcome to the phone book program.

Please choose one of the following:

1) Add New Phone Number
2) List Phone Numbers
3) Find Phone Number by Name
4) Delete Phone Number by Name
5) Quit

Please enter 1, 2, 3, 4 or 5: 2
CSO       2358-6333
FO        2358-6418
HRO       2358-6580
ITSC      2358-6188
SAO       2358-0842
```

```console
Please choose one of the following:

1) Add New Phone Number
2) List Phone Numbers
3) Find Phone Number by Name
4) Delete Phone Number by Name
5) Quit

Please enter 1, 2, 3, 4 or 5: 1
Please enter the name: F0
Please enter the number: 2358-0000
Phone number entry already exists!
```

The display on the left shows the current numbers in the phone book and the display on the right is what you see when you try to add a duplicated entry to the phone book.

### Listing Current Phone Numbers

This feature is almost the same as the simple phone book program. The minor difference is that each phone number entry is printed with the phone number properly aligned in the extended phone book program.

### Finding a Phone Number by Name

This is a new feature in the extended phone book program. You can give a name to the program and the program will find and show the corresponding phone number entry on the screen, like this:

```console
Welcome to the phone book program.

Please choose one of the following:

1) Add New Phone Number
2) List Phone Numbers
3) Find Phone Number by Name
4) Delete Phone Number by Name
5) Quit

Please enter 1, 2, 3, 4 or 5: 2
CSO       2358-6333
FO        2358-6418
HRO       2358-6580
ITSC      2358-6188
SAO       2358-0842
```

```console
Please choose one of the following:

1) Add New Phone Number
2) List Phone Numbers
3) Find Phone Number by Name
4) Delete Phone Number by Name
5) Quit

Please enter 1, 2, 3, 4 or 5: 3
Please enter the name: HRO
HRO       2358-6580
```

The display on the left shows the current numbers in the phone book and the display on the right shows what you see when you find a number by providing an appropriate name.

### Deleting a Phone Number by Name

This is also a new feature in the extended phone book program. You can now delete an existing phone number entry by providing the name of the entry to the program. For example, this is what you see in the program:

```console
Welcome to the phone book program.

Please choose one of the following:

1) Add New Phone Number
2) List Phone Numbers
3) Find Phone Number by Name
4) Delete Phone Number by Name
5) Quit

Please enter 1, 2, 3, 4 or 5: 2
CSO       2358-6333
FO        2358-6418
HRO       2358-6580
ITSC      2358-6188
SAO       2358-0842
```

```console
Please choose one of the following:

1) Add New Phone Number
2) List Phone Numbers
3) Find Phone Number by Name
4) Delete Phone Number by Name
5) Quit

Please enter 1, 2, 3, 4 or 5: 4
Please enter the name: ITSC
```

```console
Welcome to the phone book program.

Please choose one of the following:

1) Add New Phone Number
2) List Phone Numbers
3) Find Phone Number by Name
4) Delete Phone Number by Name
5) Quit

Please enter 1, 2, 3, 4 or 5: 2
CSO       2358-6333
FO        2358-6418
HRO       2358-6580
SAO       2358-0842
```

The display on the left is the current phone numbers in the program. The middle display shows the request for deleting the phone entry with the name 'ITSC'. The corresponding phone entry is then deleted as shown in the display on the right.

### The PhoneBookEntry Class

A new class __PhoneBookEntry__ has been given to you. Objects created from this class are used to store the phone number entries inside the code. The objects can then be used to handle the printing of the phone number entries as well as reading the phone number entries from the text file. You __don't__ need to change this class file in the exercise.

## Task 1. Checking for Duplicated Entry

At the moment if you run the phone book program you will be able to add entries with the same name. If you look at the __addNumber__ method you can see that it contains this code:

```Java
// Check whether the name already exists, if so,
// print a message and exit the method
if (exists(name)) {
    System.out.println("Phone number entry already exists!");
    return;
}
```

As you can see, we have already included the checking for duplicated name for you. Why doesn't it work then? It is because the __exists__ method, which has been used in the above code, is empty.

Your task now is the finish the __exists__ method so that the code inside the __addNumber__ method works.

### The __exists__ Method

The __exists__ method works like this. It reads the data file __phonebook.txt__ line by line. While reading the lines, it checks whether the name in the entry is the same as the one you want to add from the __addNumber__ method. If they are the same, the new phone number is a duplicated entry. In this situation, the __exists__ method returns true to indicate that there is a duplicated entry in the phone book. If, after reading the entire phone book, you cannot find any entry using the same name, the __exists__ method will return false to indicate that you can now add the new entry in the phone book.

### Reading the Data File

You can read the data file __phonebook.txt__ using a __BufferedReader__. We have already used similar code to read the file when we list the current phone numbers from the phone book. If you look at the code in the __listNumbers__ method you will see the method first gets the __BufferedReader__ and then uses the __BufferedReader__ to read and print the phone number entries.

Here is the while loop used to read the text file in __listNumbers__:

```Java
// Read the content line-by-line and print it out
String line;
while ((line = reader.readLine()) != null) {
    // Create a new phone book entry from the data line
    PhoneBookEntry entry = new PhoneBookEntry(line);

    // Print the phone book entry
    entry.print();
    System.out.println();
}
```

Inside the while loop the first line of code creates a __PhoneBookEntry__ object from the line of text read from the file. The __PhoneBookEntry__ object automatically extracts the name and phone number from the line of text. You can then start to use several helpful methods from the __PhoneBookEntry__ object. For example, the __listNumbers__ method uses the __print__ method to output the phone number entry nicely on the screen.

However, in the __exists__ method you don't need to print the phone number entries. What you need to do is to check whether the name in the entry is the same as the given __name__ parameter, i.e. the name you want to add to the phone book. If they are the same, you will return true to indicate the phone number entry already exists. If none of the phone book entries matches the given name, you will return false.

To get the name of the phone number entry you can use the __getName__ method of the __PhoneBookEntry__ object. Be reminded that you will have to use the __equals__ method to compare the name because it is a string value, i.e.:

```Java
if (entry.getName().equals(name)) {
    ...
}
```

After you have finished the __exists__ method you will not be able to add duplicated entry in the phone book anymore.

## Task 2. Finding a Phone Number by Name

In the second task you need to find a phone number by name. The user enters the name and the program prints the corresponding phone book entry. If the name does not exist the program will show an appropriate message.

You will do this task in the __findNumberByName__ method. Inside the method, the code to get the name input is given, as shown below:

```Java
// Get the name
System.out.print("Please enter the name: ");
String name = scanner.next();
```

Using the __name__ variable you will find the phone number entry from the data file. Again, we can borrow the idea from the __listNumbers__ method. If we look at the code in the method, you will see that the __listNumbers__ method reads the entire phone book and prints all the entries out on the screen. In this task you don't need to print all entries. You only need to print the entry which matches the entered name. That means you can use most of the code from the __listNumbers__ method. The only place you need to change is to check the name of the entry before you print, like this:

```Java
if (entry.getName().equals(name)) {
    ...print the entry...
}
```

If the name of the entry is the entered name, you will first print the corresponding entry and then finish the method using a return statement, i.e.:

```Java
return;
```

If you finish reading the data file without finding the corresponding entry, you will need to print an appropriate message to show that the entry does not exist, like this:

```console
Please choose one of the following:

1) Add New Phone Number
2) List Phone Numbers
3) Find Phone Number by Name
4) Delete Phone Number by Name
5) Quit

Please enter 1, 2, 3, 4 or 5: 3
Please enter the name: ABC
Phone number entry does not exist!
```

## Task 3. Deleting a Phone Number by Name

In this task, you need to get the name entered by the user and then delete the corresponding entry in the phone book. This is more complicated than the first two tasks because the first two tasks involve reading of the data file only but this task requires writing as well.

You may think that you can use a single while loop to do both reading and writing, i.e. deleting the requested entry while going through the list of entries in the phone book. However, you cannot do that because we only have one data file. You cannot read from and write to the same file at the same time. So let's do it in two stages.

### Reading the Phone Book

Since we only have one single file, you will need to read the phone book into a temporary storage, delete the appropriate entry and then save the data back to the same file. At this stage, you will read the phone book and store it into a temporary place. The temporary place that we are going to use is an array. You can find this code in the given __deleteNumberByName__ method:

```Java
// Prepare an array to store the phone number entries
PhoneBookEntry[] entries = new PhoneBookEntry[100];

// Store the number of entries in the phone book
int numOfEntries = 0;
```

The above code creates an array of __PhoneBookEntry__. The array has a size of 100 because, in this exercise, we have assumed that the number of entries in the phone book will not exceed 100. The size of the array has been fixed at 100 so we need something to remember the actual number of entries in the phone book. The __numOfEntries__ variable is created for this purpose. It stores the actual number of entries in the phone book.

You will read the data file line by line. For each line in the file you will create a new __PhoneBookEntry__ object and put the object in the __entries__ array. You can again borrow the code we have used in the __listNumbers__ method to do that. This time, again, you don't need to print the entry inside the while loop. You will need to store the phone book entry into the array using this code:

```Java
entries[numOfEntries] = entry;
numOfEntries++;
```

The first line of above code stores the __PhoneBookEntry__ object into the array, using the position indicated by the value of __numOfEntries__. Initially the __numOfEntries__ variable is 0. That means the first time the above code is run, the __PhoneBookEntry__ object becomes the first item of the array. When you run it the second time, you should store the __PhoneBookEntry__ object in the second position of the array. Therefore, each time after you store the object in the array you need to increase the __numOfEntries__ variable by one, as shown in the second line of the above code. If you do this, the __numOfEntries__ variable will keep track of the current item you want to store the object as well as the actual number of items you have stored so far.

You don't actually need to store all phone number entries into the __entries__ array. Remember that the objective of this task is to delete one entry from the phone book, you can store all entries in the array, __except__ the one which matches the name entered by the user. You can use an if statement to do this, as shown below:

```Java
if (!entry.getName().equals(name)) {
    ...Store the object in the array...
}
```

After this stage, the __entries__ array should contain all phone number entries, except the one you want to delete.

### Writing to the Phone Book

Now that the appropriate phone number entries have been stored in the temporary place, the __entries__ array. You can save the entries back to the data file. You can use a __BufferedWriter__ to do that.

You have learned that, to get a __BufferedWriter__, you can use the following line of code \(assuming you have a correct __Path__ object\):

```Java
BufferedWriter writer =
    Files.newBufferedWriter(path, Charset.defaultCharset(), StandardOpenOption.APPEND);
```

However, you need to use a slightly different __BufferedWriter__ this time. The __BufferedWriter__ created by the above code will append any new content at the end of the file. In this task, you don't really append data to the end of the file because the __entries__ array already has __ALL__ the data. That means you need to remove the __StandardOpenOption.APPEND__ parameter so that the __BufferedWriter__ will erase the current content of the file before writing the new one.

If the __BufferedWriter__ is ready, you can use a for loop to write the entries into the file. Reminded that the number of phone book entries is stored in the __numOfEntries__ variable the for loop should run for that number of times. For each entry you need to write the content of the entry into the file using the following code, assuming __entries\[i\]__ points to the current entry in the array inside the loop:

```Java
// Add a phone number entry in a line
writer.write(entries[i].toLine());
writer.newLine();
```

After you finish writing the content of the file, you need to close the __BufferedWriter__ using the __close__ method.

## Testing Your Program

After you finish your program you should make sure that it works by adding, finding and deleting several phone number entries. You should also try to add duplicated entries as well as finding and deleting entries which do not exist in the phone book.

## Submission

You need to finish the program in a file called ___PhoneBook.java___.

__Do not__ submit ___PhoneBookEntry.java___ as you __don't__ need to change it.

After you have finished your work, upload and submit your file by clicking the "Submit Assignment", and then choosing your file to submit.

## submission

- file: [PhoneBook.java](submission/PhoneBook.java)
