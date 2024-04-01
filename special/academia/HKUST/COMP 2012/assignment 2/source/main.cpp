#include <iostream>
#include <string>
#include "userBoard.h"
using namespace std;

Piece* getPromotionPiece(Color color) {
    char c;
    do {
        cout << "Type the piece to promote to: ";
        cin >> c;
        switch (c) {
            case 'q': case 'Q':
                return new Queen(color);
            case 'n': case 'N':
                return new Knight(color);
            case 'r': case 'R':
                return new Rook(color);
            case 'b': case 'B':
                return new Bishop(color);
            default:
                cout << "Unrecognized piece." << endl;
        }
    } while (true);
}

bool isValidInput(const string& str) {
    if (str.length() != 2) {
        return false;
    }
    char file = str[0];
    char rank = str[1];
    return (file >= 'a') && (file <= 'h') && (rank >= '1') && (rank <= '8');
}

Position strToPosition(const string& str) {
    char file = str[0];
    char rank = str[1];
    return Position{static_cast<_FILE>(file - 'a'), static_cast<_RANK>(rank - '1')};
}

int main(int argc, char* argv[]) {
    WesternBoard board;

    int blankCount = 0;
    string fen;
    if (argc > 1) {
        fen = argv[1];
        cout << "Using custom FEN: " << fen << endl;
    }
    else fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1";

    for (_RANK r = _8; r >= _1; r = static_cast<_RANK>(r-1)) {
        for (_FILE f = _A; f <= _H; f = static_cast<_FILE>(f+1)) {
            if (blankCount > 0) {
                --blankCount;
                continue;
            }
            char next = fen.at(0);
            fen = fen.substr(1);

            switch (next) {        
                case 'r': case 'R': board.addPiece(new Rook(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'n': case 'N': board.addPiece(new Knight(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'b': case 'B': board.addPiece(new Bishop(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'q': case 'Q': board.addPiece(new Queen(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'k': case 'K': board.addPiece(new King(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'p': case 'P': board.addPiece(new Pawn(isupper(next) ? WHITE : BLACK), Position{f, r}); break;

                case 'a': case 'A': board.addPiece(new Compound<'A', Bishop, Knight>(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'c': case 'C': board.addPiece(new Compound<'C', Rook, Knight>(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'd': case 'D': board.addPiece(new OmniLeaper<'D', 2, 0>(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'e': case 'E': board.addPiece(new Divergent<'E', Bishop, Knight>(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'f': case 'F': board.addPiece(new OmniLeaper<'F', 1, 1>(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'g': case 'G': board.addPiece(new Compound<'G', Leaper<'G', 1, 2>, Leaper<'G', -1, 2>>(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'h': case 'H': board.addPiece(new Divergent<'H', Knight, Bishop>(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'l': case 'L': board.addPiece(new Rider<'L', 0, 1>(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'm': case 'M': board.addPiece(new OmniRider<'M', 2, 1>(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 's': case 'S': board.addPiece(new Compound<'S', OmniLeaper<'S', 1, 1>, Leaper<'S', 0, 1>>(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'w': case 'W': board.addPiece(new OmniLeaper<'W', 1, 0>(isupper(next) ? WHITE : BLACK), Position{f, r}); break;
                case 'z': case 'Z': board.addPiece(new OmniLeaper<'Z', 2, 3>(isupper(next) ? WHITE : BLACK), Position{f, r}); break;

                case '1': case '2': case '3': case '4': case '5': case '6': case '7': case '8': 
                    blankCount = next - '1';
                    break;
                default:
                    cout << "ERROR: Incorrect FEN detected." << endl;
                    exit(1);
            }

            if (fen.at(0) == '/') fen = fen.substr(1);
        }
    }

    fen = fen.substr(1);
    board.setInitialAttributes(fen);

    string input;
    while (true) {
        board.display();

        do {
            cout << "Select your piece to move: ";
            cin >> input;
            if (input == "exit")
                exit(0);
        } while (!isValidInput(input) || !board.select(strToPosition(input)));

        board.display();

        do {
            cout << "Select the destination square: ";
            cin >> input;
            if (input == "exit")
                exit(0);
        } while (!isValidInput(input) || !board.select(strToPosition(input)));
    }
}
