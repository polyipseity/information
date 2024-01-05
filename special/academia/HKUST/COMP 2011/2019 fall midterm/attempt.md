---
aliases: []
tags:
  - date/2023/09/23/from
  - date/2023/09/24/to
  - languages/in/English
---

# 2019 fall midterm attempt

HKUST COMP 2011

- time allowed: 2023-09-23T23:30:00+08:00/PT2H
- time used: 2023-09-23T23:30:00+08:00/PT1H16M
- type: practice

## problem 1 (12 points)

> 1. 1
> 2. 2
> 3. cout << 5
> 4. 6
> 5. 7
> 6. cout << 4
> 7. 5
> 8. cout << 2
> 9. 3
> 10. cout << 7
> 11. 8
>
> - answer: `5 4 2 7`

## problem 2 (9 points)

> - answer:
>   1. `int&`
>   2. `int`
>   3. `int&`

## problem 3 (18 points)

> - answer:
>   1. `1.5, -2, 1`
>   2. `1, -2, 1`
>   3. COMPILATION ERROR
>   4. `1.5, -2, 1`
>   5. `1.5, 2, 1`
>   6. `1, 2, 1`

## problem 4 (16 points)

> - answer:
>   1. `(0, 2)`
>   2. `(0, 3)`
>   3. `(1, 2)`
>   4. `(1, 1)`
>   5. `(1, 0)`
>   6. `(2, 0)`
>   7. `(2, 1)`
>   8. `(3, 1)`

## problem 5 (25 points)

### (a) (6 points)

> answer
>
> ```Cpp
> void initGame(TicTacToe& game) {
>   for (int xx{0}; xx < N; ++xx) {
>     for (int yy{0}; yy < N; ++yy) {
>       setArray(game.physicalboard[xx][yy], EMPTY);
>     }
>   }
>   setArray(game.superboard, EMPTY);
> }
> ```

### (b) (10 points)

> answer
>
> ```Cpp
> bool check3inline(const Array& array) {
>   for (int idx{0}; idx < N; ++idx) {
>     if (array[idx][0] != EMPTY && same(array[idx][0], array[idx][1], array[idx][2])) {
>       return true;
>     }
>     if (array[0][idx] != EMPTY && same(array[0][idx], array[1][idx], array[2][idx])) {
>       return true;
>     }
>   }
>   if (array[0][0] != EMPTY && same(array[0][0], array[1][1], array[2][2])) {
>     return true;
>   }
>   if (array[0][2] != EMPTY && same(array[0][2], array[1][1], array[2][0])) {
>     return true;
>   }
>   return false;
> }
> ```

### (c) (9 points)

> answer
>
> ```Cpp
> void printBoards(const TicTacToe& game) {
>   const char symbol[] = {' ', 'X', 'O'}; // ' ': empty, 'X': player1, 'O': player2
>   cout << "Physical board:" << endl;
>   cout << "   0  1  2   3  4  5   6  7  8" << endl;
>   cout << " |---------|---------|---------|" << endl;
>   // YOUR CODE STARTS HERE
>   for (int row{0}; row < N * N; ++row) {
>     cout << row << '|';
>     for (int col{0}; col < N * N; ++col) {
>       cout << ' ' << symbol[game.physicalboard[row / N][col / N].grid[row % N][col % N]] << ' ';
>       if ((col + 1) % N == 0) {
>         cout << '|';
>       }
>     }
>     cout << endl;
>     if ((row + 1) % N == 0) {
>       cout << " |---------|---------|---------|" << endl;
>     }
>   }
> }
> ```

## problem 6 (20 points)

### (a) (2 points)

> answer: 45432

### (b) (4 points)

> answer
>
> ```Cpp
> int string2int(const char s[], int x[]) {
>   int idx{0};
>   for (; s[idx] != '\0'; ++idx) {
>     x[idx] = s[idx] - '0';
>   }
>   return idx;
> }
> ```

#### (c) (7 points)

> answer
>
> ```Cpp
> bool is_pingpong(const int x[], int num_digits, int stepsize, int diff) {
>   if (stepsize >= num_digits) { return true; }
>   int difference{x[stepsize] - x[0]};
>   difference = difference < 0 ? -difference : difference;
>   if (difference != diff) { return false; }
>   return is_pingpong(x + 1, num_digits - 1, stepsize, diff);
> }
> ```

#### (d) (7 points)

> answer
>
> ```Cpp
> void to_pingpong(int x[], int num_digits) {
>   if (is_pingpong(x, num_digits, 1, 1)) { return; }
>   to_pingpong(x, num_digits - 1);
>   int expect{x[num_digits - 2] - 1};
>   x[num_digits - 1] = expect < 0 ? x[num_digits - 2] + 1 : expect;
> }
> ```
