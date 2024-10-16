#include "lab5_functions.h" // Include the declearation of the function


// detect corner points of the possible rectangle
// corner points are inclusive to the possible rectangle
// corner_points[0]: row index of the top left corner
// corner_points[1]: column index of the top left corner
// corner_points[2]: row index of the bottom right corner
// corner_points[3]: column index of the bottom right corner
void detect_corner(const int arr[][MAX_DIMENSION], int row, int col, int corner_points[]) {
    /***************Start your code here***************/
    [arr, col, corner_points, row]()
    {
        for (int row_cur{}; row_cur < row; ++row_cur)
        {
            for (int col_cur{}; col_cur < col; ++col_cur)
            {
                if (arr[row_cur][col_cur])
                {
                    corner_points[0] = row_cur;
                    corner_points[1] = col_cur;
                    return;
                }
            }
        }
    }();
    [arr, col, corner_points, row]()
    {
        for (int row_cur{row - 1}; row_cur >= 0; --row_cur)
        {
            for (int col_cur{col - 1}; col_cur >= 0; --col_cur)
            {
                if (arr[row_cur][col_cur])
                {
                    corner_points[2] = row_cur;
                    corner_points[3] = col_cur;
                    return;
                }
            }
        }
    }();
    /***************End your code here***************/
}