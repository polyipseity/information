#include <iostream>
#include "board.h"
#include "piece.h"
#include "taskProgress.h"
using namespace std;

/**
 * Add a piece to the specified position.
 * 
 * If the position already contains a piece, output message, deallocate the piece and return.
 * Otherwise, set the pointer at the position to point to the piece.
 * 
 * If the piece is "royal", also set the corresponding royalPieces pointer to point to it.
 * We check if the piece is royal using the global isRoyal() function, which the user needs to
 * implement in userPiece.cpp. There can only be one royal piece per player.
 * This is disabled if you have not completed task 4 yet.
*/
void Board::addPiece(Piece* piece, const Position& pos)
{
    if (this->piece(pos)) {
        cout << "ERROR: Board already contains piece at position " << pos << endl;
        delete piece;
        return;
    }
#ifdef TASK4_1_2_PIECES_COMPLETE
    if (isRoyal(piece)) {
        if (royalPieces[piece->getColor()]) {
            cout << "ERROR: There already is a royal piece added." << endl;
            delete piece;
            return;
        }
        else {
            royalPieces[piece->getColor()] = piece;
        }
    }
#endif
    this->piece(pos) = piece; 
    piece->setPosition(pos);
}

/**
 * Select the specified position.
 * The function returns true if the selection is successful.
 * 
 * If selectedPiece is nullptr:
 * - Return false if the position contains no piece, or has an opponent piece.
 * - Otherwise, the piece is selected. Set moveMap accordingly, and call validateMoveMap()
 *   to remove moves that put the current player's royal piece in check. Then return true.
 * 
 * If selectedPiece is not nullptr:
 * - If the position is the same as selectedPiece, reset selectedPiece and moveMap and return true.
 *   This allows the player to unselect and try a different piece.
 * - Else, if moveMap at the specified position is false, return false as the selectedPiece cannot be moved there.
 *   Otherwise, call move(), then reset selectedPiece and moveMap and return true.
*/
bool Board::select(const Position& pos)
{
    if (!selectedPiece) {
        if (!piece(pos)) {
            cout << "No piece here." << endl;
            return false;
        }

        if (piece(pos)->isWhite() ^ isWhiteTurn) {
            cout << "This is the opponent's piece." << endl;
            return false;
        }

        cout << "Selecting " << pos << endl;
        selectedPiece = piece(pos);
        moveMap = piece(pos)->getMoves(*this);
        validateMoveMap();
    }
    else {
        if (piece(pos) == selectedPiece) {
            cout << "Unselecting " << pos << endl;
            selectedPiece = nullptr;
            moveMap = BooleanMap{};
            return true;
        }

        if (!moveMap.cell(pos)) {
            cout << "This piece cannot be moved here." << endl;
            return false;
        }

        cout << "Moving " << selectedPiece->getPosition() << " to " << pos << endl;
        move(pos);
        selectedPiece = nullptr;
        moveMap = BooleanMap{};
    }
    return true;
}

/**
 * Return a board where the newPiece is placed at the specified position.
 * Creates a Board using the copy constructor, deletes the piece at the specified position if necessary,
 * then add the newPiece to the specified position and return this board.
 * 
 * This function can be used for scenarios such as "if this piece was at this position, what would be its moveset".
*/
Board Board::getTempBoard(Piece* newPiece, const Position& pos) const
{
    Board temp {*this};
    if (temp.piece(pos)) {
        if (temp.selectedPiece == temp.piece(pos)) temp.selectedPiece = newPiece;
        if (temp.royalPieces[newPiece->getColor()] == temp.piece(pos)) temp.royalPieces[newPiece->getColor()] = newPiece;
        delete temp.piece(pos);
        temp.piece(pos) = nullptr;
    }
    temp.addPiece(newPiece, pos);
    return temp;
}

/**
 * Return a BooleanMap indicating which cells contain an opponent piece.
 * @param white: Whether the "player" is White or Black. If the player is White,
 *              return the map of all Black pieces.
*/
BooleanMap Board::getOpponentMap(bool white) const
{
    BooleanMap map{};
    for (_RANK r = _8; r >= _1; r = static_cast<_RANK>(r-1)) {
        for (_FILE f = _A; f <= _H; f = static_cast<_FILE>(f+1)) {
            if (piece(f, r) && (piece(f, r)->isWhite() ^ white))
                map.cell(f, r) = true;
        }
    }
    return map;
}

/**
 * Displays the board.
 * 
 * If a piece is selected, it will be highlighted with ( ) brackets.
 * Squares that piece can move to are highlighted with . if they are empty, or
 * [ ] brackets if they contain a piece. This is checked using the moveMap
 * data member, so it should be updated whenever selectedPiece is set.
*/
void Board::display() const {
    cout << "Current turn: " << (isWhiteTurn ? "White" : "Black") << endl;

    for (int i=0; i<4*NUM_FILES+1; ++i) 
        cout << '-';
    cout << endl;

    int rankNum = 8;
    for (_RANK r = _8; r >= _1; r = static_cast<_RANK>(r-1)) {
        for (_FILE f = _A; f <= _H; f = static_cast<_FILE>(f+1)) {
            cout << '|';
            cout << (selectedPiece && piece(f, r) == selectedPiece ? '(' : (moveMap.cell(f, r) && piece(f, r) ? '[' : ' '));
            cout << (piece(f, r) ? piece(f, r)->getName() : (moveMap.cell(f, r) ? '.' : ' '));
            cout << (selectedPiece && piece(f, r) == selectedPiece ? ')' : (moveMap.cell(f, r) && piece(f, r) ? ']' : ' '));
        }
        cout << "| " << rankNum-- << endl;
        for (int i=0; i<4*NUM_FILES+1; ++i) 
            cout << '-';
        cout << endl;
    }

    char fileChar = 'a';
    for (_FILE f = _A; f <= _H; f = static_cast<_FILE>(f+1)) {
        cout << "  " << fileChar++ << ' ';
    }
    cout << endl;
}
