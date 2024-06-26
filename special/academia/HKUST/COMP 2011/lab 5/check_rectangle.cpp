#include "lab5_functions.h" // Include the declearation of the function

// You need to make sure the detected corner_points not form a line or point
bool check_rectangle(const int arr[][MAX_DIMENSION], int row, int col, int corner_points[]) {
    /***************Start your code here***************/
    if (corner_points[0] == corner_points[2] || corner_points[1] == corner_points[3])
    {
        return false;
    }
    for (int row_cur{}; row_cur < row; ++row_cur)
    {
        for (int col_cur{}; col_cur < col; ++col_cur)
        {
            if ((corner_points[0] <= row_cur && row_cur <= corner_points[2] && corner_points[1] <= col_cur && col_cur <= corner_points[3]) != static_cast<bool>(arr[row_cur][col_cur]))
            {
                return false;
            }
        }
    }
    return true;
    /***************End your code here***************/
}