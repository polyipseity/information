#ifndef MATRIX_H
#define MATRIX_H

#include <iostream>

using namespace std;

template<typename T>
void stupid_swap(T &left, T &right)
{
    T temp{left};
    left = right;
    right = temp;
}

template <typename T>
class Matrix {
private:
    size_t rows, cols;
    T* data;
    T dummy; // Dummy value for out-of-bounds access


public:

    // Parameterized constructor for creating a matrix with given dimensions
    Matrix(size_t rows, size_t cols) : rows(rows), cols(cols), data(new T[rows * cols]), dummy(T()){}


    Matrix(const Matrix& other) : rows(other.rows), cols(other.cols), data(new T[other.rows * other.cols]) {
        for (size_t i = 0; i < rows * cols; ++i) {
            data[i] = other.data[i];
        }
    }

    ~Matrix() {
        delete[] data;
    }

    // TODO1: Implement the assignment operator for the Matrix class
    // This operator should replace the current Matrix's contents with the contents of another Matrix.
    // It needs to safely handle self-assignment, release the current memory, and allocate new memory to hold the copied data.

    Matrix& operator=(const Matrix& other) {
    /*
    ...
    */
        Matrix temp{other};
        stupid_swap(rows, temp.rows);
        stupid_swap(cols, temp.cols);
        stupid_swap(data, temp.data);
        stupid_swap(dummy, temp.dummy);
        return *this;
    }

    T& operator()(size_t row, size_t col) {
        if (row >= rows || col >= cols) {
            cerr << "Matrix subscript out of bounds" << endl;
            return dummy;
        }
        return data[row * cols + col];
    }

    const T& operator()(size_t row, size_t col) const {
        if (row >= rows || col >= cols) {
            cerr << "Matrix subscript out of bounds" << endl;
            return dummy;
        }
        return data[row * cols + col];
    }

    // TODO2: Implement the output operator to print the matrix to an ostream
    // You should iterate over each element of the matrix, printing each row on a new line.
    // Each element should be separated by a space.

    friend ostream& operator<<(ostream& os, const Matrix<T>& matrix) {
    /*
    ...
    */
        for (size_t row{}; row < matrix.rows; ++row)
        {
            for (size_t col{}; col < matrix.cols; ++col)
            {
                if (col > 0)
                    os << ' ';
                os << matrix(row, col);
            }
            if (row < matrix.rows - 1)
                os << '\n';
        }
        os << flush;
        return os;
    }


    // TODO3.1: Implement the addition operator to add two matrices
    // We assume both matrices have the same dimensions before performing the addition.
    Matrix<T> operator+(const Matrix<T>& rhs) const {
        cout << "Performing addition operation" << endl;
    /*
    ...
    */
        Matrix temp{*this};
        for (size_t row{}; row < rows; ++row)
        {
            for (size_t col{}; col < cols; ++col)
                temp(row, col) += rhs(row, col);
        }
        return temp;
    }

    // TODO3.2: Implement the subtraction operator to subtract one matrix from another
    // We assume both matrices have the same dimensions before performing the subtraction.

    Matrix<T> operator-(const Matrix<T>& rhs) const {
        cout << "Performing subtraction operation" << endl;
    /*
    ...
    */

        Matrix temp{*this};
        for (size_t row{}; row < rows; ++row)
        {
            for (size_t col{}; col < cols; ++col)
                temp(row, col) -= rhs(row, col);
        }
        return temp;
    }

    // TODO4: Implement the multiplication operator to multiply two matrices
    // We assume the number of columns in the first matrix equal the number of rows in the second matrix.
    // The resulting matrix should have the number of rows of the first matrix and the number of columns of the second matrix.

    Matrix<T> operator*(const Matrix<T>& rhs) const {
        cout << "Performing multiplication operation" << endl;
    /*
    ...
    */

        Matrix temp{rows, rhs.cols};
        for (size_t row{}; row < rows; ++row)
        {
            for (size_t col{}; col < rhs.cols; ++col)
            {
                temp(row, col) = T{};
                for (size_t com{}; com < cols; ++com)
                    temp(row, col) += (*this)(row, com) * rhs(com, col);
            }
        }
        return temp;
    }

    // TODO5: Implement the inversion operator (~) to calculate the inverse of a 2x2 matrix
    // We assume the matrix is a invertible 2x2 matrix
    Matrix<T> operator~() const {
        cout << "Performing inversion operation" << endl;
    /*
    ...
    */
        T det{(*this)(0, 0) * (*this)(1, 1) - (*this)(0, 1) * (*this)(1, 0)};
        Matrix temp{2, 2};
        temp(0, 0) = (*this)(1, 1) / det;
        temp(0, 1) = -(*this)(0, 1) / det;
        temp(1, 0) = -(*this)(1, 0) / det;
        temp(1, 1) = (*this)(0, 0) / det;
        return temp;
    }

};


#endif // MATRIX_H
