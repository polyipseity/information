/*

  The following program solves the L-shape blocks problem

   Given
          A 2^N x 2^N array (In this assignment, we restrict the value N as 1, 2
  and 3 ) The location of the empty cell (x,y) The legal (x,y) coordinates of
  the empty cell:

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
// The function returns after getting valid values for width, emptyXPos and
// emptyYPos
int locateQuadrant(int width, int x, int y)
{
  int hw = width / 2;
  if (x < hw && y < hw)
  {
    return 1;
  }
  if (x >= hw && y < hw)
  {
    return 2;
  }
  if (x >= hw && y >= hw)
  {
    return 3;
  }
  return 4; // bottom-left quad

  // remove this line to start your work
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

/**
 * Helper function for normalizePuzzleMap.
 */
char getReplacement(char original, char charArray[MAX_WIDTH * MAX_WIDTH])
{
  for (int x = 0; x < MAX_WIDTH * MAX_WIDTH; x++)
  {
    if (charArray[x] == ' ' || charArray[x] == original)
    {
      charArray[x] = original;
      return 'A' + x;
    }
  }
  // This function should never get here!
  return 'z';
}

/**
 * Normalize the whole puzzleMap. The space character ' ' will not be changed.
 */
void normalizePuzzleMap(int width, char puzzleMap[][MAX_WIDTH])
{
  char charArray[MAX_WIDTH * MAX_WIDTH];
  // Initialize the charArray to empty
  for (int x = 0; x < MAX_WIDTH * MAX_WIDTH; x++)
  {
    charArray[x] = ' ';
  }

  for (int y = 0; y < width; y++)
  {
    for (int x = 0; x < width; x++)
    {
      if (puzzleMap[x][y] == ' ')
      {
        continue;
      }
      puzzleMap[x][y] = getReplacement(puzzleMap[x][y], charArray);
    }
  }
  return;
}

/**
 * [The most important function in this program]
 * The recursive function to fill up the character array: puzzleMap
 */
void fillPuzzleRecursive(int width, char puzzleMap[][MAX_WIDTH], int tx, int ty,
                         int x, int y, char &nextChar)
{
  // tx: top Left X coordinate
  // ty: top Left Y coordinate
  // x:  x coordinate of the empty cell
  // y:  y coordinate of the empty cell
  if (width == 2)
  {
    // The base case...
    for (int i = 0; i < 2; i++)
    {
      for (int j = 0; j < 2; j++)
      {
        if (tx + i == x && ty + j == y)
        {
          //  do nth..
        }
        else
        {
          puzzleMap[tx + i][ty + j] = nextChar;
        }
      }                      // end for j
    }                        // end for i
    nextChar = nextChar + 1; // move to the next char
    return;
  }
  // The general case
  int hw = width / 2; // half width

  // Remember the fill character
  char fillChar = nextChar;
  nextChar = nextChar + 1;

  // The return value: quad
  // MUST be equal to 1, 2, 3 or 4
  int quad = locateQuadrant(width, x - tx, y - ty);
  // cout << "Quad: " << quad << endl;
  //
  // Key idea:
  //  Because qual must be equal to either 1, 2, 3 or 4
  // As a result:
  //    A L-shape MUST be created at the center of the bigger rectangle
  //    Each Quad MUST have exactly 1 empty space

  if (quad == 1)
  {
    fillPuzzleRecursive(hw, puzzleMap, tx, ty, x, y, nextChar);
  }
  else
  {
    // Drill a new empty space
    puzzleMap[tx + hw - 1][ty + hw - 1] = fillChar;
    // Recursively solve the problem
    fillPuzzleRecursive(hw, puzzleMap, tx, ty, tx + hw - 1, ty + hw - 1,
                        nextChar);
  }

  if (quad == 2)
  {
    fillPuzzleRecursive(hw, puzzleMap, tx + hw, ty, x, y, nextChar);
  }
  else
  {
    // Drill a new empty space
    puzzleMap[tx + hw][ty + hw - 1] = fillChar;

    // Recursively solve the problem
    fillPuzzleRecursive(hw, puzzleMap, tx + hw, ty, tx + hw, ty + hw - 1,
                        nextChar);
  }

  if (quad == 3)
  {
    fillPuzzleRecursive(hw, puzzleMap, tx + hw, ty + hw, x, y, nextChar);
  }
  else
  {
    // Drill a new empty space
    puzzleMap[tx + hw][ty + hw] = fillChar;

    // Recursively solve the problem
    fillPuzzleRecursive(hw, puzzleMap, tx + hw, ty + hw, tx + hw, ty + hw,
                        nextChar);
  }

  if (quad == 4)
  {
    fillPuzzleRecursive(hw, puzzleMap, tx, ty + hw, x, y, nextChar);
  }
  else
  {
    // Drill a new empty space
    puzzleMap[tx + hw - 1][ty + hw] = fillChar;

    // Recursively solve the problem
    fillPuzzleRecursive(hw, puzzleMap, tx, ty + hw, tx + hw - 1, ty + hw,
                        nextChar);
  }
  return;
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
// The function returns after getting valid values for width, emptyXPos and
// emptyYPos
void checkInput(int &width, int &emptyXPos, int &emptyYPos)
{
  // Some helper lines for you to use:
  // cout << "Enter the width/height of the puzzle (2, 4, 8): ";
  // cout << "Enter the x-coordinate of the empty cell (0-" << width - 1 << "):
  // "; cout << "Enter the y-coordinate of the empty cell (0-" << width - 1 <<
  // "): ";

  do
  {
    cout << "Enter the width/height of the puzzle (2, 4, 8): ";
    cin >> width;
    cout << endl;
  } while (width != 2 && width != 4 && width != 8);

  do
  {
    cout << "Enter the x-coordinate of the empty cell (0-" << width - 1
         << "): ";
    cin >> emptyXPos;
    cout << endl;
  } while (emptyXPos < 0 || emptyXPos >= width);

  do
  {
    cout << "Enter the y-coordinate of the empty cell (0-" << width - 1
         << "): ";
    cin >> emptyYPos;
    cout << endl;
  } while (emptyYPos < 0 || emptyYPos >= width);
  return;
}

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
    cout << "0: Exit directly (for testing checkInput function), 1: Output "
            "Quadrant of the empty cell,"
         << endl
         << "2: Output without normalization (for student's debug only), 3: "
            "Output with normalization"
         << endl;
    cout << "Enter the output mode: ";
    cin >> modeOfOperation;
    cout << endl;
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
