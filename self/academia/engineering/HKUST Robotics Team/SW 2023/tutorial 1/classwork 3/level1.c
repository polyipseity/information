#include <stdio.h>

int main()
{
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
  printf("I am a year %d student with GPA %.1f.", year, GPA);
  // your code ends here
  return 0;
}
