#include <iostream>
#include "board.h"
#include "piece.h"
using namespace std;

/**
 * TASK 2.1: Board copy constructor
*/
Board::Board(const Board& board)
{
    // TODO
}

/**
 * TASK 2.2: Board destructor
*/
Board::~Board() 
{
    // TODO
}

/**
 * TASK 4.1: Board::move(const Position&)
*/
void Board::move(const Position& destPos)
{
    // Safeguard against misusage of move()
    if (!selectedPiece) {
        cout << "ERROR: Piece not selected, cannot call move()" << endl;
        return;
    }

    // TODO
}

/**
 * TASK 4.2: Board::getAttackingMap() const
*/
BooleanMap Board::getAttackingMap() const
{
    // TODO
    return BooleanMap{};
}

/**
 * TASK 4.3: Board::validateMoveMap()
*/
void Board::validateMoveMap()
{
    // TODO
}

