---
aliases: []
tags:
  - date/2023/09/24
  - language/in/English
---

<!-- markdownlint-disable MD024 MD036 -->

# 2018 spring final attempt

HKUST COMP 2011

- [attempt](attempt.md) · [check](check.md)
- time allowed: 2023-09-24T16:00:00+08:00/PT2H30M
- time used: 2023-09-24T16:00:00+08:00/PT1H50M28S
- type: test

## problem 1 (20 points)

### (a) (2 points)

Make the function accept two references to number types in its parameters like `void func(int &outA, int &outB)`.

### (b) (3 points)

- `a[0]`: `3`
- `a[1]`: `4`
- `a[2]`: `6`
- `a[3]`: `6`
- `a[4]`: `7`

### (c) (3 points)

```console
12
```

### (d) (6 points)

```Cpp
void swapParts(int array[], int cut, int size) {
  for (int ii{0}; ii < cut; ++ii) {
    int first{array[0]};
    for (int jj{1}; jj < size; ++jj) {
      array[jj - 1] = array[jj];
    }
    array[size - 1] = first;
  }
}
```

### (e) (6 points)

```Cpp
void fun(int arr[], int size) {
  int ii{0};
  for (; ii < size / 2; ++ii) {
    int product{arr[ii] * arr[size - 1 - ii]};
    arr[ii] = arr[size - 1 - ii] = product;
  }
  if (size % 2) {
    arr[ii] *= arr[ii];
  }
}
```

## problem 2 (20 points)

### (a) (2 points)

Add a `if` check representing the base case that does not call the recursive function itself again. Also, all inputs to the recursive function should eventually lead to the base case so that it terminates on all inputs.

### (b) (3 points)

It calculates the sum of 10 dice rolls, treating odd rolls ($i\in{1,3,5,7,9}$) as positive and even rolls ($i\in{2,4,6,8,10}$) as negative.

### (c) (3 points)

It runs forever in theory and usually crashes due to stack overflow in practice. There is no base case that does not call the function itself in the function definition.

### (d) (6 points)

```Cpp
int minionDice(int level) {
  if (level >= NDICE) { return 0; }
  int dices[NDICE]{};
  for (int ii{0}; ii <= level; ++ii) {
    dices[ii] = 1 + rand() % 6;
  }
  cout << "level " << level << ':';
  for (int ii{0}; ii <= level; ++ii) {
    cout << ' ' << dices[ii];
  }
  cout << endl;
  int sum{0};
  for (int ii{0}; ii <= level; ++ii) {
    sum += dices[ii];
    if (dices[ii] == 6) {
      sum += minionDice(level + 1);
    }
  }
  return sum;
}
```

### (e) (6 points)

```Cpp
void recursiveSort(int arr[], int size, int index) {
  if (index >= size) { return; }
  int minIdx{index};
  for (int ii{index + 1}; ii < size; ++ii) {
    if (arr[ii] < arr[minIdx]) {
      minIdx = ii;
    }
  }
  int tmp{arr[minIdx]};
  arr[minIdx] = arr[index];
  arr[index] = tmp;
  recursiveSort(arr, size, index + 1);
}
```

## problem 3 (20 points)

### (a) (2 points)

The middle because two links needs to be updated instead of one for the other two options.

### (b) (3 points)

```console
fnrbs
```

__draft__

1. zmxrbsawt
2. zmxrbswt
3. zmxnrbswt
4. zmxnrbs
5. zmxfnrbs
6. fnrbs

### (c) (3 points)

It replaces the last node of the linked list `head` with a new node containing the value of `c`. If the linked list is empty (`nullptr`), then an node containing the value of `c` is set as the start of the linked list.

An memory leak may occur since the last node being replaced is not `delete`d when the linked list is non-empty.

### (d) (6 points)

```Cpp
void deleteN(ll_cnode*& head, int N) {
  ll_cnode *prev{nullptr}, *cur{head};
  for (int ii{0}; cur != nullptr && ii < N; ++ii) {
    prev = cur;
    cur = head->next;
  }
  if (cur == nullptr) { return; }
  if (prev == nullptr) {
    head = cur->next;
  } else {
    prev->next = cur->next;
  }
  delete cur;
}
```

### (e) (6 points)

```Cpp
void addWordToDictionary(wordSection d[], int size, const char* newWord) {
  wordSection &sect{d[newWord[0] - 'a']};
  if (sect.num == 0) {
    sect.words = new char*[++sect.num];
  } else {
    char **oldWords{sect.words};
    sect.words = new char*[++sect.num];
    for (int ii{0}; ii < (sect.num - 1); ++ii) {
      sect.words[ii] = oldWords[ii];
    }
    delete[] oldWords;
  }
  sect.words[sect.num - 1] = new char[strlen(newWord) + 1];
  strcpy(sect.words[sect.num - 1], newWord);
}
```

## problem 4 (20 points)

### (a) (2 points)

A `Lamp` has a variable number of `Bulb`s.

### (b) (3 points)

```console
2200 810
```

### (c) (3 points)

```Cpp
Lamp:@:Lamp(int n, float p) {
  // Answer here:
  max_num_bulbs = n;
  price = p;
  bulbs = new Bulb[n];
  num_bulbs = 0;
}
```

### (d) (6 points)

```Cpp
void Lamp:@:add_bulbs(int w, float p, int n) {
  if ((max_num_bulbs - num_bulbs) < n) { return; }
  for (int ii{0}; ii < n; ++ii) {
    bulbs[num_bulbs++].set(w, p);
  }
}
```

### (e) (6 points)

```Cpp
float Lamp:@:total_price() const {
  // Answer here:
  const ret{price};
  for (int ii{0}; ii < num_bulbs; ++ii) {
    ret += bulbs[ii].get_price();
  }
  return ret;
}
```

## problem 5 (20 points)

### (a) (2 points)

A stack is last-in-first-out while a queue is first-in-first-out.

### (b) (3 points)

```console
No. of data currently on the queue = 4 Front item = 1
Empty: false  Full: false
```

__draft__

1. 5, 3
2. 3
3. 3, 7, 1
4. 3, 7, 1, n = 3
5. 3, 7, 1, 3, 9, n = 3
6. 7, 1, 3, 9, n = 3
7. 7, 1, 3, 9, n = 4
8. 7, 1, 3, 9, 4, n = 4
9. 1, 3, 9, 4, n = 4

### (c) (3 points)

It returns the number of items in the priority queue that has a higher priority than `n` (smaller value than `n`).

### (d) (6 points)

```Cpp
char priority_queue:@:dequeue() {
  // Answer here:
  if (head == nullptr) { return '\0'; }
  ll_cnode *cur{head};
  char ret{cur->data};
  head = cur->next;
  delete cur;
  return ret;
}
```

### (e) (6 points)

```Cpp
void priority_queue:@:enqueue(char d, int p) {
  // Answer here:
  ll_cnode *prev{nullptr};
  for (ll_cnode *cur{head}; cur != nullptr; prev = cur, cur = cur->next) {
    if (p < cur->priority) { break; }
  }
  if (prev == nullptr) {
    head = new ll_cnode{d, p, nullptr};
    return;
  }
  prev->next = new ll_cnode{d, p, prev->next};
}
```
