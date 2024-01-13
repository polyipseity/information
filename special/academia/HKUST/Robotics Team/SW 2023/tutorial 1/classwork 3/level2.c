#include <stdio.h>

int main()
{
  float gpa;
  int year;
  printf("What is your GPA: ");
  scanf("%g", &gpa);
  printf("What is your year: ");
  scanf("%d", &year);
  printf("I am a year %d student with GPA %.1f.", year, gpa);
  return 0;
}
