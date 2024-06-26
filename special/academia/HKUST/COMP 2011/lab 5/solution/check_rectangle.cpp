#include "lab5_functions.h" // Include the declearation of the function

// You need to make sure the detected corner_points not form a line or point
bool check_rectangle(const int arr[][MAX_DIMENSION], int row, int col, int corner_points[]) {
    /***************Start your code here***************/
    bool is_rectangle = true;

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (i >= corner_points[0] && j >= corner_points[1] && i <= corner_points[2] && j <= corner_points[3]) {
                if (arr[i][j] == 0) {
                    is_rectangle = false;
                }
            } else {
                if (arr[i][j] == 1) {
                    is_rectangle = false;
                }
            }
        }
    }
    if (corner_points[2] == corner_points[0] || corner_points[3] == corner_points[1]) {
        is_rectangle = false;
    }
    return is_rectangle;
    /***************End your code here***************/
}