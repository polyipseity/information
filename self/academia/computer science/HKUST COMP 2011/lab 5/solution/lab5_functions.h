// The following #ifndef/#define/#endif is used to avoid multiple include during the separate compilation
// Please don't delete these statements

#ifndef LAB5_FUNCTIONS_H  
#define LAB5_FUNCTIONS_H

const int MAX_DIMENSION = 8;

void detect_corner(const int arr[][MAX_DIMENSION], int row, int col, int corner_points[]);
bool check_rectangle(const int arr[][MAX_DIMENSION], int row, int col, int corner_points[]);
int area_size(const int arr[][MAX_DIMENSION], int row, int col, const int corner_points[]);

#endif // LAB5_FUNCTIONS_H