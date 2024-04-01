#ifndef __PIECE_H__
#define __PIECE_H__

#include "board.h"

// Maximum range of a Rider piece
const int MAX_RANGE = NUM_FILES > NUM_RANKS ? NUM_FILES : NUM_RANKS;

// Enum representing a piece's color
// Can also be used for Board's royalPieces array: royalPieces[WHITE] is White's royal piece
enum Color { BLACK, WHITE };


// Base class for all chess pieces
class Piece {
    private:
        // Pure virtual private function that returns a character representing this piece
        // Concrete derived classes need to implement this function
        virtual char name() const = 0;

    protected:
        // The piece's current position. Needs to be updated whenever this piece moves
        Position position;
        // The piece's color
        Color color;

    public:
        // Constructor: sets the piece's color. Position will need to be set later
        Piece(Color color): color(color) {}

        // Virtual destructor: Default
        virtual ~Piece() = default;

        // Pure virtual function that returns a dynamic-allocated instance of the concrete derived class
        virtual Piece* clone() const = 0;

        // Returns the character representing this piece (uppercase for white, lowercase for black) 
        char getName() const { return name() - (isWhite() ? 0 : 'A' - 'a'); }

        // Accessor functions
        Position getPosition() const { return position; }
        Color getColor() const { return color; }

        // Convenient functions to check if piece is White, or if another piece is the opponent's piece
        bool isWhite() const { return color == WHITE; }
        bool isOpponent(const Piece& other) const { return color != other.color; }

        // Mutator function for the position
        void setPosition(const Position& pos) { position = pos; }

        // Pure virtual function that returns a BooleanMap indicating where this piece can move to
        virtual BooleanMap getMoves(const Board& board) const = 0;
};

// Template class that derives Piece and implements the name() function
template <char N>
class NamedPiece : public Piece {
    private:
        virtual char name() const override { return N; }
    
    public:
        NamedPiece(Color color): Piece(color) {}
};


// The following 4 template classes will need to be implemented in pieceToImplement.h
template <char N, int F, int R>
class Leaper;

template <char N, int F, int R, int RANGE = MAX_RANGE>
class Rider;

template <char N, typename P1, typename P2>
class Compound;

template <char N, typename M, typename C>
class Divergent;

#include "pieceToImplement.h"


// Aliases for OmniLeaper and OmniRider
template<char N, int F, int R>
using OmniLeaper = Compound<N,                                              \
                    Compound<N,                                             \
                        Compound<N, Leaper<N, F, R>, Leaper<N, R, F>>,      \
                        Compound<N, Leaper<N, -F, R>, Leaper<N, R, -F>>     \
                    >,                                                      \
                    Compound<N,                                             \
                        Compound<N, Leaper<N, F, -R>, Leaper<N, -R, F>>,    \
                        Compound<N, Leaper<N, -F, -R>, Leaper<N, -R, -F>>   \
                    >                                                       \
                >;

template<char N, int F, int R, int RANGE = MAX_RANGE>
using OmniRider = Compound<N,                                                           \
                    Compound<N,                                                         \
                        Compound<N, Rider<N, F, R, RANGE>, Rider<N, R, F, RANGE>>,      \
                        Compound<N, Rider<N, -F, R, RANGE>, Rider<N, R, -F, RANGE>>     \
                    >,                                                                  \
                    Compound<N,                                                         \
                        Compound<N, Rider<N, F, -R, RANGE>, Rider<N, -R, F, RANGE>>,    \
                        Compound<N, Rider<N, -F, -R, RANGE>, Rider<N, -R, -F, RANGE>>   \
                    >                                                                   \
                >;


#endif // __PIECE_H__