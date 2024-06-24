/*
 * Lab 1 Solution
 * A program to compute the perimeter of a rectangle given the width and height
 */
#include <iostream>
using namespace std;

int main()
{
    int width, height; // Define 2 variables that will hold the width and height respectively

    cout << "Please input the width of the rectangle: ";
    cin >> width;
    cout << "Please input the height of the rectangle: ";
    cin >> height;

    if ((width <= 0) || (height <= 0)) // check if width or height is zero or negative
    {
        cout << "Error: the width and height must be positive!" << endl;
    }
    else
    {
        cout << "The perimeter of the rectangle is " << 2 * (width + height) << endl;
    }

    return 0;
}