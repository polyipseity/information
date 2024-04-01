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


// TODO 1.2: Vector::operator+(const Position&) const


// TODO 1.3: Vector::operator*(int) const


// TODO 1.4: BooleanMap::operator|=(const BooleanMap&)


// TODO 1.5: BooleanMap::operator&=(const BooleanMap&)


// TODO 1.6: BooleanMap::operator~() const

