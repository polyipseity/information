#define _USE_MATH_DEFINES
#include <math.h>
#include <stdio.h>
#include <stdbool.h>

// your function starts here
float circleArea(float radius)
{
  return M_PI * radius * radius;
}
// your function ends here

int main()
{
  printf("%f", circleArea(5.0f));
  return 0;
}
