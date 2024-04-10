#include "matrix.h"
#include <iostream>
using namespace std;

int main() {

    cout << "\n================================Case1================================\n";
    // case 1 Constructing copying and printing matrices
    Matrix<int> mat1(2, 2);
    mat1(0, 0) = 1; mat1(0, 1) = 2;
    mat1(1, 0) = 10; mat1(1, 1) = 4;

    Matrix<double> mat2(2, 2);
    mat2(0, 0) = 5; mat2(0, 1) = 4.3;
    mat2(1, 0) = 3.7; mat2(1, 1) = 8.2;

    Matrix<double> mat3(2, 2);
    mat3 = mat2;

    cout << "Matrix 1:\n" << mat1 << endl;
    cout << "Matrix 2:\n" << mat2 << endl;
    cout << "Matrix 3:\n" << mat3 << endl;
    cout << "\n================================Case2================================\n";

    // case 2 Addition and Substraction operation

    Matrix<double> matA(4, 4);
    Matrix<double> matB(4, 4);

    for (size_t i = 0; i < 4; ++i) {
        for (size_t j = 0; j < 4; ++j) {
            matA(i, j) = i * 4 + j + 1; 
        }
    }

    for (size_t i = 0; i < 4; ++i) {
        for (size_t j = 0; j < 4; ++j) {
            matB(i, j) = (i * 4 + j + 1) * 2; 
        }
    }

    cout << "Matrix A:\n" << matA << endl;
    cout << "Matrix B:\n" << matB << endl;

    Matrix<double> sumResult = matA + matB;

    cout << "Result of Addition:\n" << sumResult << endl;


    Matrix<double> subtractionResult = matA - matB;

    cout << "Result of Subtraction:\n" << subtractionResult << endl;

    cout << "\n================================Case3================================\n";

    // case 3 Multiplication operation
        
    Matrix<double> matC(2, 3); // Matrix of 2 rows and 3 columns
    matC(0, 0) = 1; matC(0, 1) = 2; matC(0, 2) = 3;
    matC(1, 0) = 4; matC(1, 1) = 5; matC(1, 2) = 6;

    Matrix<double> matD(3, 2); // Matrix of 3 rows and 2 columns
    matD(0, 0) = 7; matD(0, 1) = 8;
    matD(1, 0) = 9; matD(1, 1) = 10;
    matD(2, 0) = 11; matD(2, 1) = 12;

    cout << "Matrix C:\n" << matC << endl;
    cout << "Matrix D:\n" << matD << endl;


    Matrix<double> multiplicationResult = matC * matD;
    
    cout << "Multiplication Result:\n" << multiplicationResult << endl;



    cout << "\n================================Case4================================\n";

    // case 4 Inversion operation (valid only for 2x2 matrices)

    Matrix<double> matInvertible(2, 2);
    matInvertible(0, 0) = 4; matInvertible(0, 1) = 7;
    matInvertible(1, 0) = 2; matInvertible(1, 1) = 6;


    cout << "Original Matrix:\n" << matInvertible << endl;
    Matrix<double> inverseResult = ~matInvertible;

    cout << "Inversion Result:\n" << inverseResult << endl;
}
