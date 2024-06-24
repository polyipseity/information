#ifndef __USERPIECE_H__
#define __USERPIECE_H__

#include "piece.h"

bool isRoyal(const Piece* piece);

// The following 2 classes are given as example
using Knight = OmniLeaper<'N', 2, 1>;

using Rook = OmniRider<'R', 1, 0>;

// TASK 4.1: Define the 3 classes Bishop, Queen, King similar to above
// TODO
using Bishop = OmniRider<'B', 1, 1>;
using Queen = Compound<'Q', Rook, Bishop>;
using King = Compound<'K', OmniLeaper<' ', 1, 0>, OmniLeaper<' ', 1, 1>>;



// TASK 4.3: Define the Pawn class
// TODO
class Pawn : public Divergent<'P', Leaper<' ', 0, 1>, Compound<' ', Rider<' ', -1, 1, 2>, Rider<' ', 1, 1, 2>>>
{
public:
  using Divergent::Divergent;

  Pawn *clone() const override
  {
    return new Pawn{*this};
  }

  BooleanMap getMoves(Board const &board) const override
  {
    BooleanMap ret{Divergent::getMoves(board)};
    if (color == Color::WHITE)
    {
      if (position.rank == _2 && !board.piece(position.file, _3) && !board.piece(position.file, _4))
      {
        ret.cell(position.file, _4) = true;
      }
    }
    else if (position.rank == _7 && !board.piece(position.file, _6) && !board.piece(position.file, _5))
    {
      ret.cell(position.file, _5) = true;
    }
    return ret;
  }
};





#endif // __USERPIECE_H__