---
aliases: []
tags:
  - date/2023/09/26
  - languages/in/English
---

<!-- markdownlint-disable MD024 -->

# Classwork 3 : Introduce Yourself

!Nice to meet you!

## LEVEL 1

Add a print statement below such that `GPA` and `year` are printed.

```C
#include <stdio.h>

int main() {
  /**
  * By adding const here, your gpa freezes and will always be 4.3!
  * Adding const makes the variable *constant* throughout the program.
  */
  const float GPA = 4.3f;

  /**
  * If const was added here, you'll always be a year 1 student,
  * so you can't graduate!
  */
  int year = 1;

  // your code starts here

  // your code ends here
  return 0;
}
```

### Example Output

```console
I am a year 1 student with GPA 4.3.
```

## LEVEL 2

This time you are required to implement an interactive program. The program should ask for your current GPA and current year, save the information into the corresponding variables, then print the variables on a new line.

### Example Output

```console
What is your GPA: 4.0
What is your year: 2
I am a year 2 stduent with GPA 4.0.
```

`What is your GPA:` and `What is your year:` should be printed by your program.

#### Reminder

- You can make the program based on the first `Introduce Yourself`.
- `scanf` reads the console input and save the information to variables

---

<https://hkust-robotics-team.gitbook.io/hkust-robotics-team-software-tutorial/tutorial-1-c-and-dev-env-setup/classwork/classwork-3-introduce-yourself>
