/*

  The following program solves the L-shape blocks problem

   Given
	  A 2^N x 2^N array (In this assignment, we restrict the value N as 1, 2 and 3 )
	   The location of the empty cell (x,y)
		  The legal (x,y) coordinates of the empty cell:

			  For a 2 x 2 block, the legal range is 0-1
			  For a 4 x 4 block, the legal range is 0-3
			  For a 8 x 8 block, the legal range is 0-7
	   You can assume all the input values are correct

	Output:

	  The empty cell (x,y) remains empty
	  All other cells are filled by non-overlapping L-shape blocks

	Output mode:
	  (0) Console output without normalization
	  (1) Console output with normalization

	   Author: Peter, Brian, Tommy
*/

#include <iostream>
using namespace std;

// Constants in global scope
const int MAX_WIDTH = 8;
const int LOCATEQUADRANT_NOT_IMPLEMENTED = 0;

// my helpers
struct Position
{
	int x, y;
	constexpr Position &operator+=(Position const &right)
	{
		x += right.x;
		y += right.y;
		return *this;
	}
	constexpr Position &operator-=(Position const &right)
	{
		x -= right.x;
		y -= right.y;
		return *this;
	}
	constexpr Position &operator*=(int right)
	{
		x *= right;
		y *= right;
		return *this;
	}
	constexpr friend Position operator+(Position left, Position const &right)
	{
		left += right;
		return left;
	}
	constexpr friend Position operator-(Position left, Position const &right)
	{
		left -= right;
		return left;
	}
	constexpr friend Position operator*(Position left, int right)
	{
		left *= right;
		return left;
	}
	constexpr friend Position operator*(int left, Position right)
	{
		right *= left;
		return right;
	}
};
class Map
{
	char (*map)[MAX_WIDTH];
	Position base;

public:
	constexpr explicit Map(char map[][MAX_WIDTH], Position base = {}) : map{map}, base{base} {}
	constexpr char &operator[](Position const &pos)
	{
		Position const abs{to_absolute(pos)};
		return map[abs.x][abs.y];
	}
	constexpr char const &operator[](Position const &pos) const
	{
		Position const abs{to_absolute(pos)};
		return map[abs.x][abs.y];
	}
	constexpr Position to_relative(Position const &pos) const
	{
		return pos - base;
	}
	constexpr Position to_absolute(Position const &pos) const
	{
		return pos + base;
	}
};
enum struct Quadrant : int
{
	topLeft = 1,
	topRight = 2,
	bottomLeft = 4,
	bottomRight = 3,
};
constexpr Position const quadrantOffset[]{
		{-2147483648, -2147483648},
		{0, 0},
		{1, 0},
		{1, 1},
		{0, 1},
};

// TODO:
// function locateQuadrant:
// @param x:  x coordinate of the empty cell
// @param y:  y coordinate of the empty cell
//
// If x < half width, y < half width, then return 1
// If x >= half width, y < half width, then return 2
// If x >= half width, y >= half width, then return 3
// If x < half width, y >= half width, then return 4
//
// @return: int
// The function returns after getting valid values for width, emptyXPos and emptyYPos
int locateQuadrant(int width, int x, int y)
{

	// remove this line to start your work
	int const halfWidth{width / 2};
	if (x < halfWidth && y < halfWidth)
		return static_cast<int>(Quadrant::topLeft);
	if (x >= halfWidth && y < halfWidth)
		return static_cast<int>(Quadrant::topRight);
	if (x >= halfWidth && y >= halfWidth)
		return static_cast<int>(Quadrant::bottomRight);
	if (x < halfWidth && y >= halfWidth)
		return static_cast<int>(Quadrant::bottomLeft);
	return LOCATEQUADRANT_NOT_IMPLEMENTED;
}

/**
	Given the puzzleMap (2D array from the recursive function),
	Generate the console output
 */
void visualizePuzzleByText(int width, char puzzleMap[][MAX_WIDTH])
{

	cout << "  ";
	for (int x = 0; x < width; x++)
		cout << x << " ";
	cout << endl;

	for (int y = 0; y < width; y++)
	{
		cout << y << ":";
		for (int x = 0; x < width; x++)
			cout << puzzleMap[x][y] << " ";
		cout << endl;
	}
}

/**
 * Initialize the whole puzzleMap using by a space character: ' '
 */
void initializePuzzleMap(int width, char puzzleMap[][MAX_WIDTH])
{
	for (int x = 0; x < width; x++)
		for (int y = 0; y < width; y++)
			puzzleMap[x][y] = ' ';
}

// TODO:
// Normalize the whole puzzleMap. The space character ' ' will not be changed.
//
void normalizePuzzleMap(int width, char puzzleMap[][MAX_WIDTH])
{
	bool visited[MAX_WIDTH][MAX_WIDTH]{};
	char curChar{'A'};
	for (int yy{}; yy < width; ++yy)
	{
		for (int xx{}; xx < width; ++xx)
		{
			bool &thisVisited{visited[xx][yy]};
			if (thisVisited)
				continue;
			thisVisited = true;
			char &thisChar{puzzleMap[xx][yy]};
			if (thisChar == ' ')
				continue;
			for (Position const &extOffset : {
							 Position{1, 0},
							 Position{-1, 1},
							 Position{0, 1},
							 Position{1, 1},
					 })
			{
				Position const extPos{Position{xx, yy} + extOffset};
				if (!(0 <= extPos.x && extPos.x < width && 0 <= extPos.y && extPos.y < width))
					continue;
				bool &extVisited{visited[extPos.x][extPos.y]};
				char &extChar{puzzleMap[extPos.x][extPos.y]};
				if (extVisited || extChar != thisChar)
					continue;
				extVisited = true;
				extChar = curChar;
			}
			thisChar = curChar;
			++curChar;
		}
	}
}

// TODO:
// [The most important function in this program]
// The recursive function to fill up the character array: puzzleMap
// You need to figure out the parameters of the fillPuzzleRecursive function by yourself
//
void fillPuzzleRecursive(int width, char puzzleMap[][MAX_WIDTH], int tx,
												 int ty, int x, int y, char &nextChar)
{
	// tx: top Left X coordinate
	// ty: top Left Y coordinate
	// x:  x coordinate of the empty cell
	// y:  y coordinate of the empty cell
	Map map{puzzleMap, {tx, ty}};
	Position const empty{map.to_relative({x, y})};
	if (width == 2)
	{
		// The base case...
		char const emptyPrev{map[empty]};
		for (int yy{}; yy < width; ++yy)
		{
			for (int xx{}; xx < width; ++xx)
			{
				map[{xx, yy}] = nextChar;
			}
		}
		map[empty] = emptyPrev;
		++nextChar;
		return;
	}

	// The general case
	//
	// Key idea:
	//  Because qual must be equal to either 1, 2, 3 or 4
	// As a result:
	//    A L-shape MUST be created at the center of the bigger rectangle
	//    Each Quad MUST have exactly 1 empty space
	int const halfWidth{width / 2};
	Quadrant const quad{static_cast<Quadrant>(locateQuadrant(width, empty.x, empty.y))};
	for (Quadrant const curQuad : {Quadrant::topLeft, Quadrant::topRight, Quadrant::bottomRight, Quadrant::bottomLeft})
	{
		Position const &relOffset{quadrantOffset[static_cast<int>(curQuad)]};
		Position const relBase{halfWidth * relOffset},
				relEmpty{curQuad == quad ? empty : Position{halfWidth - 1, halfWidth - 1} + relOffset},
				absBase{map.to_absolute(relBase)},
				absEmpty{map.to_absolute(relEmpty)};
		fillPuzzleRecursive(halfWidth, puzzleMap, absBase.x, absBase.y, absEmpty.x, absEmpty.y, nextChar);
	}
	Position const relBase{halfWidth - 1, halfWidth - 1},
			absBase{map.to_absolute(relBase)},
			absEmpty{absBase + quadrantOffset[static_cast<int>(quad)]};
	fillPuzzleRecursive(2, puzzleMap, absBase.x, absBase.y, absEmpty.x, absEmpty.y, nextChar);
}

// TODO:
// function checkInput:
//
// @param width: the width of the square. Valid values: 2, 4, 8
// You can assume inputs are always integers.
// @param emptyXPos: the x-axis of the empty position.
// Valid range: [0, width-1].
// You can assume inputs are always integers.
// @param emptyYPos: the y-axis of the empty position.
// Valid range: [0, width-1].
// You can assume inputs are always integers.
//
//  Note: The pass-by-reference variables will be used in the main function.
// @return: void
// The function returns after getting valid values for width, emptyXPos and emptyYPos
void checkInput(int &width, int &emptyXPos, int &emptyYPos)
{
	// Some helper lines for you to use:
	width = emptyXPos = emptyYPos = -1;
	do
	{
		cout << "Enter the width/height of the puzzle (2, 4, 8): ";
		cout << endl;
		cin >> width;
	} while (!(width == 2 || width == 4 || width == 8));
	do
	{
		cout << "Enter the x-coordinate of the empty cell (0-" << width - 1 << "): ";
		cout << endl;
		cin >> emptyXPos;
	} while (!(0 <= emptyXPos && emptyXPos < width));
	do
	{
		cout << "Enter the y-coordinate of the empty cell (0-" << width - 1 << "): ";
		cout << endl;
		cin >> emptyYPos;
	} while (!(0 <= emptyYPos && emptyYPos < width));
}

// You are NOT ALLOWED to modify the main function
int main()
{

	int width = 0;
	int emptyXPos = 0;
	int emptyYPos = 0;

	checkInput(width, emptyXPos, emptyYPos);

	// initialized with empty spaces..
	char puzzleMap[MAX_WIDTH][MAX_WIDTH];

	// initialize
	initializePuzzleMap(width, puzzleMap);

	int modeOfOperation = 0;
	do
	{
		cout
			<< "0: Exit directly (for testing checkInput function), 1: Output Quadrant of the empty cell,"
			<< endl
			<< "2: Output without normalization (for student's debug only), 3: Output with normalization"
			<< endl;
		cout << "Enter the output mode: ";
		cin >> modeOfOperation;
	} while (modeOfOperation < 0 || modeOfOperation > 3);

	if (modeOfOperation == 0)
	{
		return 0;
	}
	if (modeOfOperation == 1)
	{
		int quad = locateQuadrant(width, emptyXPos, emptyYPos);
		cout << "Quadrant for the empty cell: " << quad << endl;
		return 0;
	}
	char nextChar = 'A';

	// invoke the recursive call here...
	// Result: puzzleMap will be filled by characters
	fillPuzzleRecursive(width, puzzleMap, 0, 0, emptyXPos, emptyYPos, nextChar);

	int quad = locateQuadrant(width, emptyXPos, emptyYPos);
	cout << "Quadrant for the empty cell: " << quad << endl;
	if (modeOfOperation == 2)
	{
		visualizePuzzleByText(width, puzzleMap);
	}
	else
	{
		normalizePuzzleMap(width, puzzleMap);
		visualizePuzzleByText(width, puzzleMap);
	}
	return 0;
}
