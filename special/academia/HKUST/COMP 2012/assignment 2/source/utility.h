#ifndef __COORDINATES_H__
#define __COORDINATES_H__

#include <iostream>

// Constants representing size of the board
const int NUM_RANKS = 8;
const int NUM_FILES = 8;

// Enums to indicate position on the board
enum _FILE { _A, _B, _C, _D, _E, _F, _G, _H };
enum _RANK { _1, _2, _3, _4, _5, _6, _7, _8 };

// Represents a position on the board
struct Position {
    _FILE file;
    _RANK rank;

    friend std::ostream& operator<<(std::ostream& os, const Position& pos);

    bool operator==(const Position& pos) const;
};

// Represents a direction vector from one Position to another
struct Vector {
    int file;
    int rank;

    Position operator+(const Position& pos) const;
    Vector operator*(int mul) const;
};

// An 8x8 boolean array with bitwise logical operations
class BooleanMap {
    private:
        // Initializes all cells to false by default
        bool cells[NUM_RANKS][NUM_FILES] {};

    public:
        bool& cell(_FILE f, _RANK r) { return cells[r][f]; }
        bool& cell(const Position& pos) { return cells[pos.rank][pos.file]; }
        bool cell(_FILE f, _RANK r) const { return cells[r][f]; }
        bool cell(const Position& pos) const { return cells[pos.rank][pos.file]; }

        BooleanMap& operator|=(const BooleanMap& other);
        BooleanMap& operator&=(const BooleanMap& other);
        BooleanMap operator~() const;
};

#endif // __COORDINATES_H__