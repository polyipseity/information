#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const int true  = 1;
const int false = 0;

// This function prints the content of the board array. The content is
// displayed so that the top row has an index value of 0 and the bottom row
// has an index of 4. Similarly the left column has an index of 0 and the
// rightmost column has an index of 4.
void printboard(char board[5][5])
{
    int row, col;

    printf("\n");
    printf("\t ==================== \n");

    // Print the content in a tabular structure
    for (row = 0; row < 5; row++) {
        printf("\t -------------------- \n");
        printf("\t");
        for (col = 0; col < 5; col++) {
            printf("| %c ", board[row][col]);
        }
        printf("|\n");
    }

    printf("\t -------------------- \n\n");
}

// This function returns true if the input value is unique in the current
// column and row. It returns false otherwise.
int isunique(char board[5][5], int checkrow, int checkcol, char numberinchar)
{
    int  row, col;

    // Task 2 - isunique()
    // Check for the uniqueness of the number in the current row, col
    // if the input number is unique, return true, otherwise return false.

    // Check for the row using the input checkrow value

    /* Add your code here */


    // Check for the column using the input checkcol value

    /* Add your code here */


    return true;
}

// This function initializes the game board content based on the number of
// slots to fill with random numbers
void initboard(char board[5][5], int slots)
{
    int row = 0, col = 0;
    int number = 0;
    char numberinchar;

    // Task 1 - initboard()
    // Initialize the game board, filling in the specified number of slots with
    // random numbers

    // Clear the board

    /* Add your code here */


    for (int i = 0; i < slots; i++) {
        // Find a random empty slot
        // Use rand() here to find an empty slot, i.e. a slot with a space
        // The variable row and col can be used here

        /* Add your code here */


        // Generate a random UNIQUE value in the empty slot
        do {

            // Make a random number from 1 to 9

            /* Add your code here */


            // Convert the generated number (integer type) to char type
            // by adding the ASCII value of '0'
            numberinchar = number + '0';
        } while (!isunique(board, row, col, numberinchar));

        // Store the random number into the game board

        /* Add your code here */


    }
}

// This function returns true if the board is fully occupied.
// It returns false otherwise.
int isboardfull(char board[5][5])
{
    int row, col;

    // Task 3 - isboardfull()
    // Check all rows and columns for empty spaces

    /* Add your code here */


    return true;
}

int main()
{
    // This is the 5x5 game board array
    // The value in each slot can be a number from 1 to 9,
    // a space ' ' to indicate an empty slot or
    // a '?' to show the next slot to fill
    char gameboard[5][5];

    // This stores the initial number of slots to fill up
    int slots;

    // This counts the number of times the player repeats the number
    // in either a row or column
    int repeatcount = 0;

    // These variables are for getting the input
    int row, col;
    int number;
    char numberinchar;

    // This indicates whether the game is over, i.e.:
    // - the game board is full, or
    // - the player makes repetitions 3 times in rows or columns
    int gameover = false;

    // Ask the player for the initial number of filled slots
    do {
        printf("Input the initial number of filled slots (<25): ");
        scanf(" %d", &slots);
    } while (slots <= 0 || slots >= 25);

    // Randomize the random number generation
    srand(time(NULL));

    // Initialize the game board
    initboard(gameboard, slots);

    // This is the main while loop runs while the game is not over.
    // i.e. Loop until the board is full OR the player has entered a
    // value that will have more than 3 repetitions in rows or columns
    while (!gameover) {
        // Choose the next slot to be filled
        do {
            row = rand() % 5;
            col = rand() % 5;
        } while (gameboard[row][col] != ' ');

        // Put a '?' to indicate the next input slot
        gameboard[row][col] = '?';

        // Print the current game board
        printboard(gameboard);

        // Ask for the input number
        do {
            printf("Please enter a number into the slot with '?'.\n");
            printf("The value must be from 1 to 9: ");
            scanf(" %d", &number);
        } while (number <= 0 || number > 9);

        // Change the number to a char value
        numberinchar = number + '0';

        if (isunique(gameboard, row, col, numberinchar)) {
            // Put the number into the board
            gameboard[row][col] = numberinchar;
        }
        else {
            repeatcount = repeatcount + 1;

            // There is a repetition in either the row or column
            printf("Your number has caused repetition in a row or column!\n");
            printf("You have %d chances left.\n", (3 - repeatcount));

            // Reset the slot to empty
            gameboard[row][col] = ' ';
        }

        // Game over when the board is full or repeat 3 times
        if (isboardfull(gameboard) || repeatcount >= 3) {
            gameover = true;
        }
    }

    printboard(gameboard);

    // Show the game over message
    if (repeatcount >= 3)
        printf("Game over! You have made repetitions 3 times!\n");
    else
        printf("You have successfully completed this simple Sudoku!\n");
}
