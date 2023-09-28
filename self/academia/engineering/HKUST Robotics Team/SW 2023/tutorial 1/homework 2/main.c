// Please don't include any extra libraries in your homework. We already included all necessary libraries in the skeleton code.
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

#define MAZE_ROW_NUM 10
#define MAZE_COL_NUM 20

char const *const msg_prompt_input_movement = "Enter a direction to move (w: up, a: left, s: down, d: right): \n";
char const *const msg_prompt_input_treasure_location = "Please enter the row and column of the treasure\n";
char const *const msg_prompt_input_exit_direction = "Please enter the exit direction (0: up, 1: down, 2: left, 3: right)\n";
char const *const msg_congratulation = "Congratulations! You found the treasure!\n";
char const *const msg_cannot_move_left = "You cannot move left!\n";
char const *const msg_cannot_move_right = "You cannot move right!\n";
char const *const msg_cannot_move_up = "You cannot move up!\n";
char const *const msg_cannot_move_down = "You cannot move down!\n";

typedef enum direction
{
  UP,
  DOWN,
  LEFT,
  RIGHT
} direction;
direction exit_direction;
// refer to Advanced C about enums

typedef struct pos_t
{
  int y, x;
} pos_t;
pos_t pos_move(pos_t pos, direction dir)
{
  switch (dir)
  {
  case UP:
    --pos.y;
    break;
  case DOWN:
    ++pos.y;
    break;
  case LEFT:
    --pos.x;
    break;
  case RIGHT:
    ++pos.x;
    break;
  }
  return pos;
}
bool pos_equals(pos_t left, pos_t right)
{
  return left.y == right.y && left.x == right.x;
}
bool pos_valid(pos_t pos)
{
  return 0 <= pos.y && pos.y < MAZE_ROW_NUM && 0 <= pos.x && pos.x < MAZE_COL_NUM;
}

char maze[MAZE_ROW_NUM][MAZE_COL_NUM] = {'\0'};
pos_t treasure_pos;

void maze_init()
{
  for (int i = 0; i < MAZE_ROW_NUM; i++)
  {
    for (int j = 0; j < MAZE_COL_NUM; j++)
    {
      maze[i][j] = '-';
    }
  }
}

void printMaze()
{
  for (int i = 0; i < MAZE_ROW_NUM; i++)
  {
    for (int j = 0; j < MAZE_COL_NUM; j++)
    {
      printf("%c ", maze[i][j]);
    }
    printf("\n");
  }
  printf("\n");
}

void printVariables()
{
  // for your debugging purposes only
  // your final submission should not call this function
  switch (exit_direction)
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
  printf("TREASURE_ROW: %d\n", treasure_pos.y);
  printf("TREASURE_COL: %d\n", treasure_pos.x);
}

int main()
{
  char const *const msgs_cannot_move[RIGHT - UP + 1] = {msg_cannot_move_up, msg_cannot_move_down, msg_cannot_move_left, msg_cannot_move_right};
  // input TREASURE ROW, TREASURE_COL and EXIT_DIRECTION
  printf("%s", msg_prompt_input_treasure_location);
  scanf("%d", &treasure_pos.y);
  scanf("%d", &treasure_pos.x);

  printf("%s", msg_prompt_input_exit_direction);
  scanf("%d", &exit_direction);

  maze_init();
  maze[treasure_pos.y][treasure_pos.x] = 'T';
  for (direction dir = UP; dir <= RIGHT; ++dir)
  {
    pos_t wall_pos = pos_move(treasure_pos, dir);
    if (pos_valid(wall_pos))
    {
      maze[wall_pos.y][wall_pos.x] = 'B';
    }
  }
  pos_t exit_pos = pos_move(treasure_pos, exit_direction);
  if (pos_valid(exit_pos))
  {
    maze[exit_pos.y][exit_pos.x] = '-';
  }

  bool br_start = treasure_pos.y + 1 == MAZE_ROW_NUM && treasure_pos.x + 1 == MAZE_COL_NUM;
  pos_t player_pos = {.y = br_start ? MAZE_ROW_NUM - 1 : 0, .x = br_start ? MAZE_COL_NUM - 1 : 0};
  while (!pos_equals(player_pos, treasure_pos))
  {
    maze[player_pos.y][player_pos.x] = 'P';
    printMaze();
    printf("%s", msg_prompt_input_movement);
    pos_t player_pos2 = player_pos;
    for (char cc = getc(stdin); cc != EOF && cc != '\n'; cc = getc(stdin))
    {
      direction dir;
      if (cc == 'w')
      {
        dir = UP;
      }
      else if (cc == 'a')
      {
        dir = LEFT;
      }
      else if (cc == 's')
      {
        dir = DOWN;
      }
      else if (cc == 'd')
      {
        dir = RIGHT;
      }
      else
      {
        player_pos2.y = player_pos2.x = -1;
        break;
      }
      pos_t player_pos3 = pos_move(player_pos2, dir);
      if (pos_valid(player_pos3) && maze[player_pos3.y][player_pos3.x] != 'B')
      {
        player_pos2 = player_pos3;
      }
      else
      {
        printf("%s", msgs_cannot_move[dir]);
      }
    }
    if (pos_valid(player_pos2))
    {
      maze[player_pos.y][player_pos.x] = '-';
      player_pos = player_pos2;
    }
    else
    {
      for (char cc2 = getc(stdin); cc2 != EOF && cc2 != '\n'; cc2 = getc(stdin))
        ;
    }
  }
  printf("%s", msg_congratulation);

  return 0;
}
// Algorithm: Word used by programmers when they don’t want to explain what they did.
