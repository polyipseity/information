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
    *this = board;
    for (int file{}; file < NUM_FILES; ++file)
    {
        for (int rank{}; rank < NUM_RANKS; ++rank)
        {
            Piece *&cur_piece{piece(static_cast<_FILE>(file), static_cast<_RANK>(rank))};
            if (cur_piece)
                cur_piece = cur_piece->clone();
        }
    }
    if (selectedPiece)
        selectedPiece = piece(selectedPiece->getPosition());
    for (Piece *&cur_piece : royalPieces)
    {
        if (cur_piece)
            cur_piece = piece(cur_piece->getPosition());   
    }
}

/**
 * TASK 2.2: Board destructor
*/
Board::~Board() 
{
    // TODO
    for (int file{}; file < NUM_FILES; ++file)
    {
        for (int rank{}; rank < NUM_RANKS; ++rank)
            delete piece(static_cast<_FILE>(file), static_cast<_RANK>(rank));
    }
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
    Piece *&captured{piece(destPos)};
    if (captured)
    {
        if (royalPieces[captured->getColor()] == captured)
        {
            royalPieces[captured->getColor()] = nullptr;
        }
        delete captured;
    }
    piece(selectedPiece->getPosition()) = nullptr;
    captured = selectedPiece;
    selectedPiece->setPosition(destPos);
    isWhiteTurn = !isWhiteTurn;
}

/**
 * TASK 4.2: Board::getAttackingMap() const
*/
BooleanMap Board::getAttackingMap() const
{
    // TODO
    // return BooleanMap{};
    BooleanMap ret{};
    for (int file{}; file < NUM_FILES; ++file)
    {
        for (int rank{}; rank < NUM_RANKS; ++rank)
        {
            Piece const *const cur_piece{piece(static_cast<_FILE>(file), static_cast<_RANK>(rank))};
            if (cur_piece && cur_piece->isWhite() == isWhiteTurn)
                ret |= cur_piece->getMoves(*this);
        }
    }
    ret &= getOpponentMap(isWhiteTurn);
    return ret;
}

/**
 * TASK 4.3: Board::validateMoveMap()
*/
void Board::validateMoveMap()
{
    // TODO
    for (int file{}; file < NUM_FILES; ++file)
    {
        for (int rank{}; rank < NUM_RANKS; ++rank)
        {
            Position const pos{static_cast<_FILE>(file), static_cast<_RANK>(rank)};
            if (moveMap.cell(pos))
            {
                Board temp{*this};
                temp.move(pos);
                BooleanMap attacking{temp.getAttackingMap()};
                Piece const *const &royal{temp.royalPieces[isWhiteTurn ? Color::WHITE : Color::BLACK]};
                if (royal && attacking.cell(royal->getPosition()))
                    moveMap.cell(pos) = false;
            }
        }
    }
}

