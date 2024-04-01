#ifndef __USERBOARD_H__
#define __USERBOARD_H__

#include "board.h"
#include "userPiece.h"
#include <iostream>
#include <string>

// To be implemented in main
Piece* getPromotionPiece(Color color);

// Extends Board class to add international chess special rules
class WesternBoard: public Board {
    friend class BoardTester;
    
    private:
        bool castleKingside[2] {true, true};
        bool castleQueenside[2] {true, true};
        Position enPassant {_A, _1};

    protected:
        void move(const Position& destPos) override {
            // En passant capture
            if (!(enPassant == Position{_A, _1})) {
                if (dynamic_cast<Pawn*>(selectedPiece) && (destPos == enPassant)) {
                    Position capture = {enPassant.file, isWhiteTurn ? _5 : _4};
                    delete piece(capture);
                    piece(capture) = nullptr;
                }
                enPassant = {_A, _1};
            }

            // If moving to corner, castling must no longer be available
            if (destPos == Position{_H, _1}) castleKingside[WHITE] = false;
            else if (destPos == Position{_A, _1}) castleQueenside[WHITE] = false;
            else if (destPos == Position{_H, _8}) castleKingside[BLACK] = false;
            else if (destPos == Position{_A, _8}) castleQueenside[BLACK] = false;

            // Castling
            // If King is moved then castling is no longer available
            if (dynamic_cast<King*>(selectedPiece)) {
                if (destPos == Position{_G, isWhiteTurn ? _1 : _8}) {
                    if (castleKingside[selectedPiece->getColor()]) {
                        piece(_F, isWhiteTurn ? _1 : _8) = piece(_H, isWhiteTurn ? _1 : _8);
                        piece(_H, isWhiteTurn ? _1 : _8) = nullptr;
                        piece(_F, isWhiteTurn ? _1 : _8)->setPosition(Position{_F, isWhiteTurn ? _1 : _8});
                    }
                }
                castleKingside[selectedPiece->getColor()] = false;
                
                if ((destPos == Position{_C, isWhiteTurn ? _1 : _8})) {
                    if (castleQueenside[selectedPiece->getColor()]) {
                        piece(_D, isWhiteTurn ? _1 : _8) = piece(_A, isWhiteTurn ? _1 : _8);
                        piece(_A, isWhiteTurn ? _1 : _8) = nullptr;
                        piece(_D, isWhiteTurn ? _1 : _8)->setPosition(Position{_D, isWhiteTurn ? _1 : _8});
                    }
                }
                castleQueenside[selectedPiece->getColor()] = false;
            }
            // If Rook is moved then castling on that side is no longer available
            else if (dynamic_cast<Rook*>(selectedPiece)) {
                if (selectedPiece->getPosition().file == _H)
                    castleKingside[selectedPiece->getColor()] = false;
                else if (selectedPiece->getPosition().file == _A)
                    castleQueenside[selectedPiece->getColor()] = false;
            }

            // Lambda to check if another piece is the opponent's Pawn
            auto pieceIsOpponentPawn = [](Piece* piece, Piece* opponent) -> bool {
                if (!dynamic_cast<Pawn*>(opponent)) {
                    return false;
                }
                if (!piece->isOpponent(*opponent)) {
                    return false;
                }
                return true;
            };

            // If moving Pawn 2 squares and there is an opponent Pawn nearby, en passant capture is available
            if (dynamic_cast<Pawn*>(selectedPiece)) {
                if (selectedPiece->getPosition().rank == _2 && destPos.rank == _4) {
                    if (pieceIsOpponentPawn(selectedPiece, piece(Vector{-1, 2} + selectedPiece->getPosition())) ||
                        pieceIsOpponentPawn(selectedPiece, piece(Vector{1, 2} + selectedPiece->getPosition())))
                        enPassant = {selectedPiece->getPosition().file, _3};
                }
                else if (selectedPiece->getPosition().rank == _7 && destPos.rank == _5) {
                    if (pieceIsOpponentPawn(selectedPiece, piece(Vector{-1, -2} + selectedPiece->getPosition())) ||
                        pieceIsOpponentPawn(selectedPiece, piece(Vector{1, -2} + selectedPiece->getPosition())))
                        enPassant = {selectedPiece->getPosition().file, _6};
                }
            }

            // Call base class move()
            Board::move(destPos);

            // Promotion if Pawn reaches rank 1 or 8
            if (dynamic_cast<Pawn*>(selectedPiece)) {
                if (selectedPiece->getPosition().rank == _8 || selectedPiece->getPosition().rank == _1) {
                    Piece* newPiece = getPromotionPiece(selectedPiece->getColor());
                    piece(selectedPiece->getPosition()) = newPiece;
                    newPiece->setPosition(selectedPiece->getPosition());
                    delete selectedPiece;
                }
            }
        }

    public:
        WesternBoard(): Board() {}
        WesternBoard(const WesternBoard& board): Board(board), enPassant(board.enPassant) {
            for (int i=0; i<2; ++i) {
                castleKingside[i] = board.castleKingside[i];
                castleQueenside[i] = board.castleQueenside[i];
            }
        }

        bool select(const Position& pos) {
            bool success = Board::select(pos);
            if (!success || !selectedPiece) {
                return success;
            }

            // If Pawn is selected and en passant is available nearby, add it to moveMap
            if (!(enPassant == Position{_A, _1}) && dynamic_cast<Pawn*>(selectedPiece)) {
                if ((Vector{-1, selectedPiece->isWhite() ? 1 : -1} + selectedPiece->getPosition() == enPassant) ||
                    (Vector{1, selectedPiece->isWhite() ? 1 : -1} + selectedPiece->getPosition() == enPassant)) {
                    moveMap.cell(enPassant) = true;
                    validateMoveMap();
                }
            }
            // If King is selected and castling is available, add it to moveMap
            // King cannot castle in, through or out of check
            else if (dynamic_cast<King*>(selectedPiece)) {
                _RANK r = isWhiteTurn ? _1 : _8;
                if (castleKingside[selectedPiece->getColor()]) {
                    if (!piece(_G, r) && !piece(_F, r)) {
                        bool canCastle = true;
                        for (_FILE f = _E; f <= _G; f = static_cast<_FILE>(f+1)) {
                            WesternBoard temp {*this};
                            if (f != _E) temp.move(Position{f, r});
                            else temp.isWhiteTurn = !temp.isWhiteTurn;

                            BooleanMap opponentCaptureMap = temp.getAttackingMap();
                            if (opponentCaptureMap.cell(f, r))
                                canCastle = false;
                        }
                        if (canCastle)
                            moveMap.cell(_G, r) = true;
                    }
                }
                if (castleQueenside[selectedPiece->getColor()]) {
                    if (!piece(_C, r) && !piece(_D, r) && !piece(_B, r)) {
                        bool canCastle = true;
                        for (_FILE f = _E; f >= _C; f = static_cast<_FILE>(f-1)) {
                            WesternBoard temp {*this};
                            if (f != _E) temp.move(Position{f, r});
                            else temp.isWhiteTurn = !temp.isWhiteTurn;

                            BooleanMap opponentCaptureMap = temp.getAttackingMap();
                            if (opponentCaptureMap.cell(f, r))
                                canCastle = false;
                        }
                        if (canCastle)
                            moveMap.cell(_C, r) = true;
                    }
                }
            }

            return true;
        }

        // Add the board attributes to the display
        // e.g. "KQk f6" means White can castle both sides, Black can castle kingside and there is en passant capture on e6
        void display() const {
            std::cout << "Board attributes: ";
            if (castleKingside[WHITE]) std::cout << "K";
            if (castleQueenside[WHITE]) std::cout << "Q";
            if (castleKingside[BLACK]) std::cout << "k";
            if (castleQueenside[BLACK]) std::cout << "q";
            if (!castleKingside[WHITE] && !castleQueenside[WHITE] && !castleKingside[BLACK] && !castleQueenside[BLACK]) std::cout << "-";
            std::cout << " ";
            if (!(enPassant == Position{_A, _1})) std::cout << enPassant;
            else std::cout << "-";
            std::cout << std::endl;
            Board::display();
        }

        // Helper function in main for setting up initial position attributes
        // Uses FEN notation: https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
        void setInitialAttributes(const std::string& fenAttributes) {
            std::string fen = fenAttributes;
            if (fen.at(0) == 'b') isWhiteTurn = !isWhiteTurn;

            fen = fen.substr(2);
            if (fen.at(0) == 'K') {
                fen = fen.substr(1);
                castleKingside[WHITE] = dynamic_cast<King*>(piece(_E, _1)) && dynamic_cast<Rook*>(piece(_H, _1));
            }
            else
                castleKingside[WHITE] = false;
            if (fen.at(0) == 'Q') {
                fen = fen.substr(1);
                castleQueenside[WHITE] = dynamic_cast<King*>(piece(_E, _1)) && dynamic_cast<Rook*>(piece(_A, _1));
            }
            else
                castleQueenside[WHITE] = false;
            if (fen.at(0) == 'k') {
                fen = fen.substr(1);
                castleKingside[BLACK] = dynamic_cast<King*>(piece(_E, _8)) && dynamic_cast<Rook*>(piece(_H, _8));
            }
            else
                castleKingside[BLACK] = false;
            if (fen.at(0) == 'q') {
                fen = fen.substr(1);
                castleQueenside[BLACK] = dynamic_cast<King*>(piece(_E, _8)) && dynamic_cast<Rook*>(piece(_A, _8));
            }
            else
                castleQueenside[BLACK] = false;
            if (fen.at(0) == '-') 
                fen = fen.substr(2);
            else
                fen = fen.substr(1);
            
            if (fen.at(0) != '-') {
                char file = fen[0];
                char rank = fen[1];
                enPassant = {static_cast<_FILE>(file - 'a'), static_cast<_RANK>(rank - '1')};
            }
        }
};

#endif // __USERBOARD_H__
