#include "lab5_functions.h" // Include the declearation of the functions.

#include <iostream>
using namespace std;

// Separate compilation steps:
// g++ -std=c++11 -c detect_corner_points.cpp
// g++ -std=c++11 -c check_rectangle.cpp
// g++ -std=c++11 -c calculate_area_size.cpp
// g++ -std=c++11 -c main.cpp 
// g++ -std=c++11 -o lab5 main.o detect_corner_points.o check_rectangle.o calculate_area_size.o


/* YOU MUST NOT MODIFY THE MAIN FUNCTION BELOW */
int main() {
        
    int arr[MAX_DIMENSION][MAX_DIMENSION];
    int row = MAX_DIMENSION;
    int col = MAX_DIMENSION;
    cout << "Enter the elements of the array. The elements should only be 0 or 1: "<< endl;
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            cin >> arr[i][j];
        }
    }

    int corner_points[4] = {-1, -1, -1, -1};
    detect_corner(arr, row, col, corner_points);

    bool is_rectangle = check_rectangle(arr, row, col, corner_points);
    if (is_rectangle) {
        int rectangle_size = area_size(arr, row, col, corner_points);
        cout << "The corner points are: "<< endl;
        cout << corner_points[0] << " "
            << corner_points[1] << " "
            << corner_points[2] << " "
            << corner_points[3]
            << endl;
        cout << "The rectangle size is: "<< endl;
        cout << rectangle_size << endl;
    } else {
        cout << "Not rectangle" << endl;
    }
    return 0;
}
