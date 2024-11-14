---
aliases: []
tags:
  - date/2023/09/24/from
  - date/2023/09/25/to
  - language/in/English
---

<!-- markdownlint-disable MD024 MD036 -->

# 2017 fall final attempt

HKUST COMP 2011

- [attempt](attempt.md) · [check](check.md)
- time allowed: 2023-09-24T23:30:00+08:00/PT3H
- time used: 2023-09-24T23:30:00+08:00/PT1H35M39S
- type: test

## problem 1 (10 points)

1. (a) T
2. (b) F
3. (c) T
4. (d) F
5. (e) F
6. (f) F
7. (g) F
8. (h) T
9. (i) T
10. (j) F

## problem 2 (5 points)

```Cpp
int sum(int from, int to, int diff) {
  if (from > to) {
    int tmp{from};
    from = to;
    to = tmp;
  }
  int ret{0};
  for (int ii{from}; ii <= to; ii += diff) {
    ret += ii;
  }
  return ret;
}
```

## problem 3 (5 points)

```console
7 6 5 4 3 2 1 0
```

__draft__

1. a = &arr[9]
2. a = &arr[8], arr[8] = 7
3. a = &arr[7], arr[7] = 6
4. a = &arr[6], arr[6] = 5
5. a = &arr[5], arr[5] = 4
6. a = &arr[4], arr[4] = 3
7. a = &arr[3], arr[3] = 2
8. a = &arr[2], arr[2] = 1
9. a = &arr[1], arr[1] = 0

## problem 4 (4 points)

```console
Company(2)
Employee(0)
Employee(0)
~Employee(101)
~Employee(100)
~Company()
```

## problem 5 (8 points)

### (a) (3 points)

```Cpp
bool contains(const char* s, char c) {
  if (s[0] == '\0') { return false; }
  return s[0] == c || contains(s + 1, c);
}
```

### (b) (5 points)

```Cpp
int num_distinct_char(const char* s) {
  if (s[0] == '\0') { return 0; }
  return (contains(s + 1, s[0]) ? 0 : 1) + num_distinct_char(s + 1);
}
```

## problem 6 (7 points)

```Cpp
node* merge(node* head1, node* head2) {
  if (head1 == nullptr) { return head2; }
  if (head2 == nullptr) { return head1; }
  if (head1->data > head2->data) {
    node *tmp{head1};
    head1 = head2;
    head2 = tmp;
  }
  head1->next = merge(head1->next, head2);
  return head1;
}
```

## problem 7 (5 points)

1. (a) `456`
2. (b) `565`
3. (c) `456`
4. (d) COMPILATION ERROR
5. (e) `565`

## problem 8 (16 points)

### (a) (3 points)

```Cpp
class Album
{
public:
  /* Answer: */
  Album(int maxDuration);
  bool addSong(Song const &song);
  void print() const;
private:
  Song songs[MAXSONGS]; // Array of Song objects
  int numSongs; // Number of Song objects stored in the songs
  int maxDuration; // Maximum duration of the ablum in seconds
};
```

### (b) (13 points)

```Cpp
#include "Album.h"
#include <iostream>

Album:@:Album(int maxDuration): songs{}, numSongs{0}, maxDuration{maxDuration} {}
bool Album:@:addSong(Song const &song) {
  int dur{song.getDuration()};
  for (int ii{0}; ii < numSongs; ++ii) {
    dur += songs[ii].getDuration();
  }
  if (dur > maxDuration) { return false; }
  songs[numSongs++] = song;
  return true;
}
void Album:@:print() const {
  for (int ii{0}; ii < numSongs; ++ii) {
    std:@:cout << songs[ii].getTitle() << std:@:endl;
  }
}
```

## problem 9 (20 points)

### (a) (6 points)

```Cpp
bool direct_flight(const Flights& f, const char* city1, const char* city2, int& cost) {
  for (int ii{0}; ii < f.num_flights; ++ii) {
    Flight const &ff{f.flight[ii]};
    if (strcmp(city1, ff.from) || strcmp(city2, ff.to)) { continue; }
    cost = ff.cost;
    return true;
  }
  return false;
}
```

### (b) (9 points)

```Cpp
bool flight(const Flights& f, const char* city1, const char* city2, int& cost) {
  if (direct_flight(f, city1, city2, cost)) { return true; }
  for (int ii{0}; ii < f.num_flights; ++ii) {
    Flight const &ff{f.flight[ii]};
    if (strcmp(city1, ff.from)) { continue; }
    if (flight(f, ff.to, city2, cost)) {
      cost += ff.cost;
      return true;
    }
  }
  return false;
}
```

### (c) (5 points)

```Cpp
void delete_flights(Flights& f) {
  delete[] f.flight;
  f.num_flights = 0;
  for (int ii{0}; ii < f.num_cities; ++ii) {
    delete[] f.city[ii];
  }
  delete[] f.city;
  f.num_cities = 0;
}
```

## problem 10 (20 points)

### (a) (5 points)

```Cpp
int height(const btnode* root) {
  if (root == nullptr) { return 0; }
  int left{height(root->left)}, right{height(root->right)};
  return 1 + (left > right ? left : right);
}
```

### (b) (9 points)

```Cpp
void one_level_2_array(const btnode* root, int array[], int& index, int level) {
  if (level == 1) {
    array[index++] = root->data;
    return;
  }
  one_level_2_array(root->left, array, index, level - 1);
  one_level_2_array(root->right, array, index, level - 1);
}
```

### (c) (6 points)

```Cpp
int btree_2_array(const btnode* root, int array[]) {
  int hh{height(root)}, idx{0};
  for (int ii{1}; ii <= hh; ++ii) {
    one_level_2_array(root, array, idx, ii);
  }
  return idx;
}
```
