# Task 2 : Treasure hunt

> [!info]- Authors
>
> Li Chi Kin (ckliam@connect.ust.hk)

## Task

Your task is to build a simple text-based treasure hunt game. The player must navigate from their starting position to the treasure. The grid will have the following elements:

1. 'P' represents the player's current position
2. 'T' represents the location of the treasure
3. 'B' represents barriers that block the player's path
4. '-' represents an open space where the player can move

Specifically, the assignment requires the following:

1. The user inputs the location of the treasure (TREASURE_ROW, TREASURE_COL) and the exit direction (EXIT_DIRECTION).
2. Initialize the maze with a given number of rows and columns. Fill the entire maze initially with open spaces.
3. Place the treasure in the maze in the preset position.
4. Surround the treasure with north, south, east, and west barriers. One of these barriers should have an exit represented by an open space.
5. The player starts from the top-left corner of the maze (or in the bottom-right corner if the treasure is at the top-left).
6. The player moves in the maze in response to keyboard input: 'w' (up), 'a' (left), 's' (down), 'd' (right). The player cannot move into barriers or outside the maze.
7. The game continues until the player reaches the treasure.

## Assumption

1. The maze can be represented as having a fixed size of 10 rows and 20 columns.
2. Only one exit is created in the barriers surrounding the treasure. The exit is determined by user input.
3. If the player enters anything other than 'w', 'a', 's', 'd', it is considered invalid, and the player is asked for input again.

## Example video

These are just examples.

> [2023-09-18 13-36-53.mkv](2023-09-18%2013-36-53.mkv) 4MB<br/>
> Binary

> [2023-09-18 13-39-20.mkv](2023-09-18%2013-39-20.mkv) 3MB<br/>
> Binary

​---

https://hkust-robotics-team.gitbook.io/hkust-robotics-team-software-tutorial/tutorial-1-c-and-dev-env-setup/homework/task-2-treasure-hunt
