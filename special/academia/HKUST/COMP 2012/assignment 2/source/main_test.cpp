#include <iostream>
#include <string>
#include "board.h"
#include "userPiece.h"
using namespace std;

#include "taskProgress.h"

#ifdef TASK5_BOARD_FUNC_COMPLETE
#include "userBoard.h"

Piece* getPromotionPiece(Color color) {
    return new Knight(color);
}
#endif

ostream& operator<<(ostream& os, const Vector& v) {
    os << "Vector{" << v.file << ", " << v.rank << "}";
    return os;
}

ostream& operator<<(ostream& os, const BooleanMap& m) {
    os << endl;
    for (int i=0; i<4*NUM_FILES+1; ++i) 
        os << '-';
    os << endl;

    int rankNum = 8;
    for (_RANK r = _8; r >= _1; r = static_cast<_RANK>(r-1)) {
        for (_FILE f = _A; f <= _H; f = static_cast<_FILE>(f+1)) {
            os << '|';
            os << ' ';
            os << (m.cell(f, r) ? '.' : ' ');
            os << ' ';
        }
        os << "| " << rankNum-- << endl;
        for (int i=0; i<4*NUM_FILES+1; ++i) 
            os << '-';
        os << endl;
    }

    char fileChar = 'a';
    for (_FILE f = _A; f <= _H; f = static_cast<_FILE>(f+1)) {
        os << "  " << fileChar++ << ' ';
    }
    return os;
}

// A dummy piece that moves to e8 only
// For testing Board class
class DummyPiece : public Piece {
    private:
        virtual char name() const override { return 'X'; }
    
    public:
        DummyPiece(Color color): Piece(color) {}
        virtual Piece* clone() const override { return new DummyPiece{*this}; }

        virtual BooleanMap getMoves(const Board& board) const override { 
            BooleanMap map{};
            map.cell(_E, _8) = true;
            return map; 
        }
};

Position strToPosition(const string& str) {
    char file = str[0];
    char rank = str[1];
    return Position{static_cast<_FILE>(file - 'a'), static_cast<_RANK>(rank - '1')};
}

class BoardTester {
    private:
        Board board;
#ifdef TASK5_BOARD_FUNC_COMPLETE
        WesternBoard westernBoard;
#endif

    public:
        void runTestCase(int testNum) {
            switch (testNum) {
                case 0: userTest(); break;
#ifdef TASK1_UTILITY_COMPLETE
    #define TEST(X) case X: test##X(); break
#else
    #define TEST(X) case X: cout << "Unimplemented task." << endl; break
#endif
                TEST(1); TEST(2); TEST(3); TEST(4); TEST(5); TEST(6); TEST(7); TEST(8); TEST(9);
#ifdef TASK2_BOARD_COMPLETE
    #undef TEST
    #define TEST(X) case X: test##X(); break
#else
    #undef TEST
    #define TEST(X) case X: cout << "Unimplemented task." << endl; break
#endif
                TEST(10); TEST(11);
#ifdef TASK3_1_LEAPER_COMPLETE
    #undef TEST
    #define TEST(X) case X: test##X(); break
#else
    #undef TEST
    #define TEST(X) case X: cout << "Unimplemented task." << endl; break
#endif
                TEST(12); TEST(13);
#ifdef TASK3_2_RIDER_COMPLETE
    #undef TEST
    #define TEST(X) case X: test##X(); break
#else
    #undef TEST
    #define TEST(X) case X: cout << "Unimplemented task." << endl; break
#endif
                TEST(14); TEST(15); TEST(16);
#ifdef TASK3_3_COMPOUND_COMPLETE
    #undef TEST
    #define TEST(X) case X: test##X(); break
#else
    #undef TEST
    #define TEST(X) case X: cout << "Unimplemented task." << endl; break
#endif
                TEST(17);
#ifdef TASK3_4_DIVERGENT_COMPLETE
    #undef TEST
    #define TEST(X) case X: test##X(); break
#else
    #undef TEST
    #define TEST(X) case X: cout << "Unimplemented task." << endl; break
#endif
                TEST(18); TEST(19);
#if defined(TASK3_3_COMPOUND_COMPLETE) & defined(TASK3_4_DIVERGENT_COMPLETE)
    #undef TEST
    #define TEST(X) case X: test##X(); break
#else
    #undef TEST
    #define TEST(X) case X: cout << "Unimplemented task." << endl; break
#endif
                TEST(20);
#ifdef TASK4_1_2_PIECES_COMPLETE
    #undef TEST
    #define TEST(X) case X: test##X(); break
#else
    #undef TEST
    #define TEST(X) case X: cout << "Unimplemented task." << endl; break
#endif
                TEST(21); TEST(22); TEST(23); TEST(24);
#ifdef TASK4_3_PAWN_COMPLETE
    #undef TEST
    #define TEST(X) case X: test##X(); break
#else
    #undef TEST
    #define TEST(X) case X: cout << "Unimplemented task." << endl; break
#endif
                TEST(25); TEST(26);
#ifdef TASK5_BOARD_FUNC_COMPLETE
    #undef TEST
    #define TEST(X) case X: test##X(); break
#else
    #undef TEST
    #define TEST(X) case X: cout << "Unimplemented task." << endl; break
#endif
                TEST(27); TEST(28); TEST(29); TEST(30); TEST(31); TEST(32); TEST(33); TEST(34); TEST(35); TEST(36);
                default:
                    cout << "Unrecognized test case." << endl;
                    break;
            }
        }

#ifdef TASK1_UTILITY_COMPLETE
        void test1() {
            cout << "e4 == e4: " << (Position{_E, _4} == Position{_E, _4}) << endl;
        }

        void test2() {
            cout << "Vector{1, 2} + c3 = " << (Vector{1, 2} + Position{_C, _3}) << endl;
        }

        void test3() {
            cout << "Vector{-2, 0} + g5 = " << (Vector{-2, 0} + Position{_G, _5}) << endl;
        }

        void test4() {
            cout << "Vector{3, 1} + h1 = " << (Vector{3, 1} + Position{_H, _1}) << endl;
        }

        void test5() {
            cout << "Vector{1, 2} * 2 = " << (Vector{1, 2} * 2) << endl;
        }

        void test6() {
            cout << "Vector{-3, 1} * -3 = " << (Vector{-3, 1} * -3) << endl;
        }

        void test7() {
            BooleanMap map1 {};
            for (int i=0; i<64; i+=3) map1.cell(static_cast<_FILE>(i/8), static_cast<_RANK>(i%8)) = true;
            cout << "Map 1: " << map1 << endl;

            BooleanMap map2 {};
            for (int i=0; i<64; i+=4) map2.cell(static_cast<_FILE>(i/8), static_cast<_RANK>(i%8)) = true;
            cout << "Map 2: " << map2 << endl;
            
            map1 |= map2;
            cout << "Map 1 bitwise-OR Map 2: " << map1 << endl;
        }

        void test8() {
            BooleanMap map1 {};
            for (int i=0; i<64; i+=3) map1.cell(static_cast<_FILE>(i/8), static_cast<_RANK>(i%8)) = true;
            cout << "Map 1: " << map1 << endl;

            BooleanMap map2 {};
            for (int i=0; i<64; i+=4) map2.cell(static_cast<_FILE>(i/8), static_cast<_RANK>(i%8)) = true;
            cout << "Map 2: " << map2 << endl;
            
            map1 &= map2;
            cout << "Map 1 bitwise-AND Map 2: " << map1 << endl;
        }

        void test9() {
            BooleanMap map1 {};
            for (int i=0; i<64; i+=3) map1.cell(static_cast<_FILE>(i/8), static_cast<_RANK>(i%8)) = true;
            cout << "Map 1: " << map1 << endl;
            
            map1 = ~map1;
            cout << "Bitwise-NOT Map 1: " << map1 << endl;
        }
#endif

#ifdef TASK2_BOARD_COMPLETE
        void test10() {
            board.addPiece(new DummyPiece(WHITE), Position{_D, _4});
            board.display();
        }

        void test11() {
            board.addPiece(new DummyPiece(WHITE), Position{_D, _4});
            Board board2 = board;
            board2.display();
        }
#endif
        
#ifdef TASK3_1_LEAPER_COMPLETE
        void test12() {
            board.addPiece(new Leaper<'N', 2, 1>(WHITE), Position{_D, _4});
            board.select(Position{_D, _4});
            board.display();
        }

        void test13() {
            board.addPiece(new Leaper<'N', 2, 1>(BLACK), Position{_D, _4});
            board.isWhiteTurn = false;
            board.select(Position{_D, _4});
            board.display();
        }
#endif
        
#ifdef TASK3_2_RIDER_COMPLETE
        void test14() {
            board.addPiece(new Rider<'R', 1, 0>(WHITE), Position{_D, _4});
            board.select(Position{_D, _4});
            board.display();
        }

        void test15() {
            board.addPiece(new Rider<'R', 0, 2, 2>(WHITE), Position{_D, _1});
            board.select(Position{_D, _1});
            board.display();
        }

        void test16() {
            board.addPiece(new Rider<'R', 1, 0>(WHITE), Position{_C, _5});
            board.addPiece(new Rider<'N', 1, 0>(BLACK), Position{_G, _5});
            board.select(Position{_C, _5});
            board.display();
        }
#endif
        
#ifdef TASK3_3_COMPOUND_COMPLETE
        void test17() {
            board.addPiece(new Compound<'C', Leaper<'N', 2, 1>, Rider<'R', 1, 0>>(WHITE), Position{_D, _4});
            board.select(Position{_D, _4});
            board.display();
        }
#endif
        
#ifdef TASK3_4_DIVERGENT_COMPLETE
        void test18() {
            board.addPiece(new Divergent<'D', Leaper<'N', 2, 1>, Rider<'R', 1, 0>>(WHITE), Position{_D, _4});
            board.addPiece(new Leaper<'N', 1, 0>(BLACK), Position{_G, _4});
            board.select(Position{_D, _4});
            board.display();
        }

        void test19() {
            board.addPiece(new Divergent<'D', Rider<'R', 1, 0>, Leaper<'N', 2, 1>>(WHITE), Position{_D, _4});
            board.addPiece(new Leaper<'N', 1, 0>(BLACK), Position{_G, _4});
            board.select(Position{_D, _4});
            board.display();
        }
#endif
        
#if defined(TASK3_3_COMPOUND_COMPLETE) & defined(TASK3_4_DIVERGENT_COMPLETE)
        void test20() {
            board.addPiece(new Divergent<'D', Compound<'C', Leaper<'N', 2, 1>, Rider<'R', 1, 0>>, Compound<'C', Leaper<'N', -2, 1>, Rider<'R', 0, -1>>>(WHITE), Position{_D, _4});
            board.addPiece(new Leaper<'N', 1, 0>(BLACK), Position{_G, _4});
            board.addPiece(new Leaper<'N', 1, 0>(BLACK), Position{_F, _5});
            board.addPiece(new Leaper<'N', 1, 0>(BLACK), Position{_D, _2});
            board.addPiece(new Leaper<'N', 1, 0>(BLACK), Position{_B, _5});
            board.select(Position{_D, _4});
            board.display();
        }
#endif
        
#ifdef TASK4_1_2_PIECES_COMPLETE
        void test21() {
            board.addPiece(new Bishop(WHITE), Position{_D, _4});
            board.addPiece(new Knight(WHITE), Position{_F, _2});
            board.addPiece(new Knight(BLACK), Position{_F, _6});
            board.select(Position{_D, _4});
            board.display();
        }

        void test22() {
            board.addPiece(new Queen(WHITE), Position{_D, _4});
            board.addPiece(new Knight(WHITE), Position{_B, _2});
            board.addPiece(new Knight(BLACK), Position{_F, _4});
            board.select(Position{_D, _4});
            board.display();
        }

        void test23() {
            board.addPiece(new King(WHITE), Position{_D, _4});
            board.addPiece(new Knight(WHITE), Position{_D, _3});
            board.addPiece(new DummyPiece(BLACK), Position{_E, _5});
            board.select(Position{_D, _4});
            board.display();
        }

        void test24() {
            King kingPiece {WHITE};
            cout << "King is royal: " << isRoyal(&kingPiece) << endl;
        }
#endif
        
#ifdef TASK4_3_PAWN_COMPLETE
        void test25() {
            board.addPiece(new Pawn(WHITE), Position{_D, _2});
            board.addPiece(new Pawn(BLACK), Position{_E, _3});
            board.select(Position{_D, _2});
            board.display();
        }

        void test26() {
            board.addPiece(new Pawn(WHITE), Position{_D, _3});
            board.addPiece(new Pawn(BLACK), Position{_C, _4});
            board.select(Position{_D, _3});
            board.display();
        }
#endif

#ifdef TASK5_BOARD_FUNC_COMPLETE
        void task5setup(Color color) {
            board.addPiece(new Rook(WHITE), Position{_E, _3});
            board.addPiece(new King(WHITE), Position{_G, _3});
            board.addPiece(new Knight(WHITE), Position{_C, _5});
            board.addPiece(new Queen(BLACK), Position{_B, _3});
            board.addPiece(new Bishop(BLACK), Position{_B, _8});
            board.addPiece(new Pawn(BLACK), Position{_C, _7});
            board.isWhiteTurn = (color == WHITE);
        }

        void test27() {
            task5setup(WHITE);
            board.select(Position{_C, _5});
            board.display();
            board.select(Position{_E, _4});
            board.display();
        }

        void test28() {
            task5setup(BLACK);
            board.select(Position{_B, _3});
            board.display();
            board.select(Position{_E, _3});
            board.display();
        }

        void test29() {
            task5setup(WHITE);
            cout << "White's attacking map: " << board.getAttackingMap() << endl;
        }

        void test30() {
            task5setup(WHITE);
            board.select(Position{_E, _3});
            board.display();
        }

        void test31() {
            task5setup(BLACK);
            board.select(Position{_C, _7});
            board.select(Position{_C, _6});
            board.select(Position{_G, _3});
            board.display();
        }

        void testOpening(initializer_list<pair<string, string>> moves) {
            westernBoard.addPiece(new Rook(WHITE), Position{_A, _1});
            westernBoard.addPiece(new Knight(WHITE), Position{_B, _1});
            westernBoard.addPiece(new Bishop(WHITE), Position{_C, _1});
            westernBoard.addPiece(new Queen(WHITE), Position{_D, _1});
            westernBoard.addPiece(new King(WHITE), Position{_E, _1});
            westernBoard.addPiece(new Bishop(WHITE), Position{_F, _1});
            westernBoard.addPiece(new Knight(WHITE), Position{_G, _1});
            westernBoard.addPiece(new Rook(WHITE), Position{_H, _1});

            westernBoard.addPiece(new Pawn(WHITE), Position{_A, _2});
            westernBoard.addPiece(new Pawn(WHITE), Position{_B, _2});
            westernBoard.addPiece(new Pawn(WHITE), Position{_C, _2});
            westernBoard.addPiece(new Pawn(WHITE), Position{_D, _2});
            westernBoard.addPiece(new Pawn(WHITE), Position{_E, _2});
            westernBoard.addPiece(new Pawn(WHITE), Position{_F, _2});
            westernBoard.addPiece(new Pawn(WHITE), Position{_G, _2});
            westernBoard.addPiece(new Pawn(WHITE), Position{_H, _2});

            westernBoard.addPiece(new Pawn(BLACK), Position{_A, _7});
            westernBoard.addPiece(new Pawn(BLACK), Position{_B, _7});
            westernBoard.addPiece(new Pawn(BLACK), Position{_C, _7});
            westernBoard.addPiece(new Pawn(BLACK), Position{_D, _7});
            westernBoard.addPiece(new Pawn(BLACK), Position{_E, _7});
            westernBoard.addPiece(new Pawn(BLACK), Position{_F, _7});
            westernBoard.addPiece(new Pawn(BLACK), Position{_G, _7});
            westernBoard.addPiece(new Pawn(BLACK), Position{_H, _7});

            westernBoard.addPiece(new Rook(BLACK), Position{_A, _8});
            westernBoard.addPiece(new Knight(BLACK), Position{_B, _8});
            westernBoard.addPiece(new Bishop(BLACK), Position{_C, _8});
            westernBoard.addPiece(new Queen(BLACK), Position{_D, _8});
            westernBoard.addPiece(new King(BLACK), Position{_E, _8});
            westernBoard.addPiece(new Bishop(BLACK), Position{_F, _8});
            westernBoard.addPiece(new Knight(BLACK), Position{_G, _8});
            westernBoard.addPiece(new Rook(BLACK), Position{_H, _8});

            for (pair<string, string> move : moves) {
                // Uncomment the following line if you need to debug move-by-move
                // westernBoard.display();

                westernBoard.select(strToPosition(move.first));
                westernBoard.select(strToPosition(move.second));
            }

            westernBoard.display();
        }

        #define MOVE(start, dest) make_pair(#start, #dest)

        void test32() {
            testOpening({
                MOVE(e2, e4), MOVE(e7, e5), 
                MOVE(g1, f3), MOVE(b8, c6),
                MOVE(f1, b5), MOVE(g8, f6),
            });
        }

        void test33() {
            testOpening({
                MOVE(d2, d4), MOVE(d7, d5), 
                MOVE(c2, c4), MOVE(d5, c4),
                MOVE(e2, e4), MOVE(e7, e5),
                MOVE(f1, c4),
            });
        }

        void test34() {
            testOpening({
                MOVE(e2, e4), MOVE(e7, e5), 
                MOVE(d1, h5), MOVE(b8, c6),
                MOVE(f1, c4), MOVE(g8, f6),
                MOVE(h5, f7),
            });
        }

        void test35() {
            testOpening({
                MOVE(d2, d4), MOVE(d7, d5), 
                MOVE(c1, f4), MOVE(g8, f6),
                MOVE(e2, e3), MOVE(c7, c5),
                MOVE(f4, b8), MOVE(a8, b8),
                MOVE(f1, b5), MOVE(c8, d7),
            });
        }

        void test36() {
            testOpening({
                MOVE(d2, d4), MOVE(d7, d5), 
                MOVE(c2, c4), MOVE(e7, e5),
                MOVE(d4, e5), MOVE(d5, d4),
                MOVE(e2, e3), MOVE(f8, b4),
                MOVE(c1, d2), MOVE(d4, e3),
                MOVE(d2, b4), MOVE(e3, f2),
                MOVE(e1, e2), MOVE(f2, g1),
            });
        }
#endif

        void userTest() {
            // Write your own testing code here
        }

};

int main() {
    BoardTester tester;
    cout << boolalpha;
    int test;
    cin >> test;
    tester.runTestCase(test);
}
