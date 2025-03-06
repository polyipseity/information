---
aliases:
  - HKUST COMP 1029J exercise for lesson 2
tags:
  - date/2024/01/10
  - language/in/English
---

# exercise for lesson 2

- HKUST COMP 1029J

---

- title: Exercise for Lesson 2
- due: 2024-01-10T23:59:59+08:00
- points: 100
- submitting: a file upload
- file types: java
- available: until 2024-01-10T23:59:59+08:00

---

## __ASCII to Emoji__

## Introduction

![Browser Emojis](attachments/8476538.png)

Emoji are special icons commonly used in instant messaging apps and social platforms. If a person would like to express a happy feeling, he or she may prefer to type in the corresponding emoji characters, :-\), to represent a happy face. There are many different kinds of emojis, for example:

- :-\) \(happy\)
- :-\( \(sad\)
- :'\( \(crying\)
- ;-\) \(wink\)

Nowadays, many emojis are represented by images. In this exercise, you will only use text-based emojis, i.e. emojis created using simple text. You need to write a program to convert some ASCII characters into emojis. The program reads a line of text from the user. Then, for each character c in the word, do the following:

- If __c__ equals to 'h' or 'H', change it to a happy emoji: :-\)
- If __c__ equals to 'a' or 'A', change it to an angry emoji: \*^\*
- If __c__ equals to 's' or 'S', change it to a sad emoji: :-\(
- Otherwise, keep it unchanged

Let's call these letters 'h', 'H', 'a', 'A', 's' and 'S', the 'emoji letters'.

You will need to finish two tasks in this exercise:

1. Read a line of text from the user (after finishing one line the program will read another line until the user enters 'bye' as the input)
2. Convert the 'emoji letters' to emojis

## Overview

Here is the code of the starting program file:

[AsciiToEmoji.java](template/AsciiToEmoji.java)

You can create a new project and then add the file as a new class. You will finish the two tasks in the starting file.

Here is an example output of the finished program.

```console
Please enter a line of text (enter 'bye' to quit the program): Hello!
:-)ello!
Please enter a line of text (enter 'bye' to quit the program): What?
W:-)*^*t?
Please enter a line of text (enter 'bye' to quit the program): Someone changed my text!
:-(omeone c:-)*^*nged my text!
Please enter a line of text (enter 'bye' to quit the program): Oh!
0:-)!
Please enter a line of text (enter 'bye' to quit the program): bye
bye
```

## Task 1. Reading a Line of Input from the User

You can try to compile and run the given program. After you run the program you will see this output:

```console
Please enter a line of text (enter 'bye' to quit to program):
```

At this stage the program doesn't actually require you to enter anything and it finishes right away. In this task you need to add the code to ask for user input.

### Reading Text Using a Scanner

First, you need to prepare a scanner so that you can read the user input. To do that, you find the appropriate place \(near the top of the code\) and create a scanner using the following line of code, as you have seen in several examples in the course so far.

```Java
Scanner scanner = new Scanner(System.in);
```

The scanner tool has been imported at the start of the program already so you don't need to worry about that.

Then you will read the user input inside the do while loop of the program. You will add the code inside the loop because the program needs to keep on asking for the user input until the user enters 'bye', as shown in the example output above. The do while loop looks like this in the starting code:

```Java
do {
    System.out.print("Please enter a line of text (enter 'bye' to quit the program): ");
} while (false);
```

It doesn't do much apart from printing some text. One thing you should notice is the loop condition has been set to __false__. That means the loop __always__ stops running, i.e. the loop runs its content only once. You will change this condition later in this task.

You should find the right place to add the code to ask for the input from the user. You need to use __scanner.nextLine\(\)__ and then store the text into the __line__ variable which has been created for you in the code.

In this exercise, we do not use __scanner.next\(\)__ to get input as shown in the course examples. Instead, we use __scanner.nextLine\(\)__. The difference between them is that __scanner.next\(\)__ stops reading the input when it encounters an Enter key or a space, whereas __scanner.nextLine\(\)__ stops until there is an Enter key only.

### Making the Loop Condition

Now, if you want to make sure you are doing the right thing, you can quickly print the content of the __line__ variable using a simple __println__.

The final thing you need to do for this task is to use a proper loop condition instead of using __false__. As we have discussed at the start, when the user enters 'bye' the program should stop running. In other words, the loop should keep on running if the word is __NOT__ 'bye'.

The loop condition, therefore, checks whether the content of __word__ is __"bye"__ or not. You can do that using a combination of the __equals__ command and the __!__ operator. You can find similar code in some examples we have looked at before.

So this is an example output of running the program at this stage:

```console
Please enter a line of text (enter 'bye' to quit the program): Hello
Please enter a line of text (enter 'bye' to quit the program): I am happy!
Please enter a line of text (enter 'bye' to quit the program): bye
```

## Task 2. Converting the Emoji Letters to Emojis

After getting the text from the user, you will read each character from the text and then change the character to an emoji if necessary. To do that, you need to set up a for loop like this:

```Java
for (int i = 0; i < line.length(); i++) {
    . . . line.charAt(i) . . .
}
```

Inside this for loop, you can use the given __ch__ variable to store the current character, i.e. __line.charAt\(i\)__. Then, based on the content of the variable, you use a simple if statement to change the 'emoji letters' \(i.e. h, H, a, A, s and S\) into emojis. For example, you simply use this if condition to handle the 'happy' emoji:

```Java
if (ch == 'h' || ch == 'H') {
    . . . print the 'happy' emoji. . .
}
```

Apart from the emoji letters, you also need to display the remaining characters that are not the emoji letters, using an else part of the if statement.

If you have done converting the entire line of text, you should see your emoji letters from the input changing to emojis like this:

```console
Please enter a line of text (enter 'bye' to quit the program): Good morning!
Good morning!Please enter a line of text (enter 'bye' to quit the program): Oops!
Oop:-(!Please enter a line of text (enter 'bye' to quit the program):
```

From the above output, it is pretty obvious the code is missing a println somewhere after you process the text. You will need to add that appropriately to complete the program.

## Testing Your Program

After you finish your program you should make sure that it works for all the example inputs on this page. Certainly, you should also try to test your program with other inputs too. When we grade your program, apart from the examples, we will also test it against some other text.

## Submission

You need to finish the program in a __file__ called ___AsciiToEmoji.java___. __Do not submit the BlueJ project or other files.__

After you have finished your work, upload and submit your file by clicking the "Submit Assignment", and then choosing your file to submit.

## submission

- file: [AsciiToEmoji.java](submission/AsciiToEmoji.java)
