#include "userPiece.h"
#include <typeinfo>

// TASK 4.2: isRoyal(const Piece*)
// TODO
bool isRoyal(Piece const *piece)
{
  std::type_info const &piece_type{typeid(*piece)};
  return piece_type == typeid(King);
}



// TASK 4.3: Implement any Pawn function(s) here if needed

