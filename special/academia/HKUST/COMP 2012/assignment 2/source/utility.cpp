#include <iostream>
#include "utility.h"
using namespace std;

ostream& operator<<(ostream& os, const Position& pos)
{
    os << static_cast<char>(pos.file + 'a') << static_cast<char>(pos.rank + '1');
    return os;
}

// TASK 1: Implement the 6 operator overloading functions of Position, Vector and BooleanMap
// You need to write the full function prototypes and implementations


// TODO 1.1: Position::operator==(const Position&) const
bool Position::operator==(Position const &right) const
{
    return file == right.file && rank == right.rank;
}


// TODO 1.2: Vector::operator+(const Position&) const
Position Vector::operator+(Position const &right) const
{
    int const new_file{right.file + file}, new_rank{right.rank + rank};
    if (_FILE::_A <= new_file && new_file < NUM_FILES && _RANK::_1 <= new_rank && new_rank < NUM_RANKS)
    {
        return {static_cast<_FILE>(new_file), static_cast<_RANK>(new_rank)};
    }
    return right;
}


// TODO 1.3: Vector::operator*(int) const
Vector Vector::operator*(int right) const
{
    return {file * right, rank * right};
}


// TODO 1.4: BooleanMap::operator|=(const BooleanMap&)
BooleanMap &BooleanMap::operator|=(BooleanMap const &right)
{
    for (int file{}; file < NUM_FILES; ++file)
    {
        for (int rank{}; rank < NUM_RANKS; ++rank)
        {
            Position const pos{static_cast<_FILE>(file), static_cast<_RANK>(rank)};
            cell(pos) |= right.cell(pos);
        }
    }
    return *this;
}


// TODO 1.5: BooleanMap::operator&=(const BooleanMap&)
BooleanMap &BooleanMap::operator&=(BooleanMap const &right)
{
    for (int file{}; file < NUM_FILES; ++file)
    {
        for (int rank{}; rank < NUM_RANKS; ++rank)
        {
            Position const pos{static_cast<_FILE>(file), static_cast<_RANK>(rank)};
            cell(pos) &= right.cell(pos);
        }
    }
    return *this;
}


// TODO 1.6: BooleanMap::operator~() const
BooleanMap BooleanMap::operator~() const
{
    BooleanMap ret{};
    for (int file{}; file < NUM_FILES; ++file)
    {
        for (int rank{}; rank < NUM_RANKS; ++rank)
        {
            Position const pos{static_cast<_FILE>(file), static_cast<_RANK>(rank)};
            ret.cell(pos) = !cell(pos);
        }
    }
    return ret;
}

