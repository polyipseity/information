#include <stdio.h>
// #include <string.h> // uncomment this line if needed

int main()
{
  char input[] = "Welcome to HKUST Robotics Team Software Tutorial";
  printf("Before trimming: %s\n", input);

  // your code starts here
  int len = 0;
  for (; len < sizeof(input) / sizeof(char); ++len)
  {
    if (input[len] == ' ')
    {
      break;
    }
  }
  // your code ends here

  printf("After trimming: %.*s\n", len, input);
  return 0;
}
