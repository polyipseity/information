#ifndef __BOARD_H__
#define __BOARD_H__

#include <iostream>
#include "utility.h"

// Forward declaration of some class and function
class Piece;
bool isRoyal(const Piece* piece);


// Represents the chessboard
class Board {
    // This allows the BoardTester class to access and test private member functions
    friend class BoardTester;
    
    // The following data members and member functions are protected since this class can be inherited
    // It is outside of the requirements for this assignment however, so you can treat them as private
    protected:
        // ============== Data members ============== //
        // The 2D array of pieces. "nullptr" represents an empty square
        Piece* pieces[NUM_RANKS][NUM_FILES];

        // Whether the current turn is White's or Black's
        bool isWhiteTurn {true};

        // Pointer to the selected piece. If it is nullptr, no piece is currently selected
        Piece* selectedPiece {nullptr};

        // A BooleanMap representing squares the selectedPiece can move to. If no piece is selected, it is all false
        BooleanMap moveMap;

        // Pointers to "royal" pieces that must not be captured
        Piece* royalPieces[2] {nullptr, nullptr};


        // ====== Protected member functions ======== //
        // Access the 2D array by reference
        Piece*& piece(_FILE f, _RANK r) { return pieces[r][f]; }
        Piece*& piece(const Position& pos) { return pieces[pos.rank][pos.file]; }

        // Member functions to be implemented
        virtual void move(const Position& destPos);
        BooleanMap getAttackingMap() const;
        void validateMoveMap();

    public:
        // ====== Constructors and destructor ======= //
        // Default constructor: Initialize the 2D array to all nullptr
        Board(): pieces{nullptr} {}

        // Copy constructor: To be implemented
        Board(const Board& board);

        // Destructor: To be implemented
        virtual ~Board();


        // ======== Public member functions ========= //
        // Access the 2D array using const object
        const Piece* piece(_FILE f, _RANK r) const { return pieces[r][f]; }
        const Piece* piece(const Position& pos) const { return pieces[pos.rank][pos.file]; }

        // Add a piece to the specified position
        void addPiece(Piece* piece, const Position& pos);

        // Select the specified position
        // If selectedPiece is nullptr, the piece at the provided position is selected (if it belongs to the current player)
        // Otherwise, the selectedPiece moves to the provided position (if it can be moved there)
        bool select(const Position& pos);

        // Return a board where the newPiece is placed at the specified position
        Board getTempBoard(Piece* newPiece, const Position& pos) const;

        // Return a BooleanMap indicating which cells contain an opponent piece
        // If 'white' is true, cells corresponding to Black pieces will be true
        BooleanMap getOpponentMap(bool white) const;

        // Print the current board
        void display() const;
};

#endif // __BOARD_H__