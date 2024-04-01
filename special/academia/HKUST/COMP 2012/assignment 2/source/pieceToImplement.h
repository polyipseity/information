// TASK 3: Implement the 4 Piece-derived classes here
// All classes will inherit the NamedPiece class 
// and implement the remaining pure virtual functions


// TODO 3.1: Leaper class
template <char N, int F, int R>
class Leaper : public Rider<N, F, R, 1>
{
public:
  using Rider<N, F, R, 1>::Rider;

  Leaper *clone() const override
  {
    return new Leaper{*this};
  }
};


// TODO 3.2: Rider class
template <char N, int F, int R, int RANGE>
class Rider : public NamedPiece<N>
{
public:
  using NamedPiece<N>::NamedPiece;
  using NamedPiece<N>::color;
  using NamedPiece<N>::position;

  Rider *clone() const override
  {
    return new Rider{*this};
  }

  BooleanMap getMoves(Board const &board) const override
  {
    BooleanMap ret{};
    for (int mul{1}; mul <= RANGE; ++mul)
    {
      Position const new_pos{Vector{F, R} * (color == Color::BLACK ? -mul : mul) + position};
      if (new_pos == position || board.getOpponentMap(color == Color::BLACK).cell(new_pos))
        break;
      ret.cell(new_pos) = true;
      if (board.getOpponentMap(color == Color::WHITE).cell(new_pos))
        break;
    }
    return ret;
  }
};



// TODO 3.3: Compound class
template <char N, typename P1, typename P2>
class Compound : public NamedPiece<N>
{
public:
  using NamedPiece<N>::NamedPiece;
  using NamedPiece<N>::color;
  using NamedPiece<N>::position;

  Compound *clone() const override
  {
    return new Compound{*this};
  }

  BooleanMap getMoves(Board const &board) const override
  {
    P1 p1{color};
    p1.setPosition(position);
    P2 p2{color};
    p2.setPosition(position);
    BooleanMap ret{p1.getMoves(board.getTempBoard(new P1{p1}, position))};
    ret |= p2.getMoves(board.getTempBoard(new P2{p2}, position));
    return ret;
  }
};



// TODO 3.4: Divergent class
template <char N, typename M, typename C>
class Divergent : public NamedPiece<N>
{
public:
  using NamedPiece<N>::NamedPiece;
  using NamedPiece<N>::color;
  using NamedPiece<N>::position;

  Divergent *clone() const override
  {
    return new Divergent{*this};
  }

  BooleanMap getMoves(Board const &board) const override
  {
    M mover{color};
    mover.setPosition(position);
    C capturer{color};
    capturer.setPosition(position);
    BooleanMap mover_board{mover.getMoves(board.getTempBoard(new M{mover}, position))},
        capturer_board{capturer.getMoves(board.getTempBoard(new C{capturer}, position))};
    mover_board &= ~board.getOpponentMap(color == Color::WHITE);
    capturer_board &= board.getOpponentMap(color == Color::WHITE);
    mover_board |= capturer_board;
    return mover_board;
  }
};

