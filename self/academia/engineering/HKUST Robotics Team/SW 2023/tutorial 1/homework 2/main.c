// Please don't include any extra libraries in your homework. We already included all necessary libraries in the skeleton code.
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

#define MAZE_ROW_NUM 10
#define MAZE_COL_NUM 20

int TREASURE_ROW;
int TREASURE_COL;
//              0     1    2      3
enum direction
{
  UP,
  DOWN,
  LEFT,
  RIGHT
};
enum direction EXIT_DIRECTION;
// refer to Advanced C about enums

const char *const msg_prompt_input_movement = "Enter a direction to move (w: up, a: left, s: down, d: right): \n";
const char *const msg_prompt_input_treasure_location = "Please enter the row and column of the treasure\n";
const char *const msg_prompt_input_exit_direction = "Please enter the exit direction (0: up, 1: down, 2: left, 3: right)\n";
const char *const msg_congratulation = "Congratulations! You found the treasure!\n";
const char *const msg_cannot_move_left = "You cannot move left!\n";
const char *const msg_cannot_move_right = "You cannot move right!\n";
const char *const msg_cannot_move_up = "You cannot move up!\n";
const char *const msg_cannot_move_down = "You cannot move down!\n";

char MAZE[MAZE_ROW_NUM][MAZE_COL_NUM] = {};

void maze_init()
{
  for (int i = 0; i < MAZE_ROW_NUM; i++)
  {
    for (int j = 0; j < MAZE_COL_NUM; j++)
    {
      MAZE[i][j] = '-';
    }
  }
}

void printMaze()
{
  for (int i = 0; i < MAZE_ROW_NUM; i++)
  {
    for (int j = 0; j < MAZE_COL_NUM; j++)
    {
      printf("%c ", MAZE[i][j]);
    }
    printf("\n");
  }
  printf("\n");
}

void printVariables()
{
  // for your debugging purposes only
  // your final submission should not call this function
  switch (EXIT_DIRECTION)
  {
  case UP:
    printf("The exit is at the top of the treasure.\n");
    break;
  case DOWN:
    printf("The exit is at the bottom of the treasure.\n");
    break;
  case LEFT:
    printf("The exit is at the left of the treasure.\n");
    break;
  case RIGHT:
    printf("The exit is at the right of the treasure.\n");
    break;
  }
  printf("TREASURE_ROW: %d\n", TREASURE_ROW);
  printf("TREASURE_COL: %d\n", TREASURE_COL);
}

int main()
{
  // input TREASURE ROW, TREASURE_COL and EXIT_DIRECTION
  printf("%s", msg_prompt_input_treasure_location);
  scanf("%d", &TREASURE_ROW);
  scanf("%d", &TREASURE_COL);

  printf("%s", msg_prompt_input_exit_direction);
  scanf("%d", &EXIT_DIRECTION);

  maze_init();
  printMaze();
  printVariables();

  return 0;
}
// Algorithm: Word used by programmers when they don’t want to explain what they did.
