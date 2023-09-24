---
aliases: []
tags:
  - date/2023/09/24
---

# 2017 fall midterm attempt

_HKUST COMP 2011_

- [attempt](attempt.md) · [check](check.md)
- time allowed: 2023-09-24T07:00:00+08:00/PT2H
- time used: 2023-09-24T07:00:00+08:00/PT1H14M49S
- type: test

## problem 1 (10 points)

__answer__

```Cpp
switch (word[i]) {
	case 'a':
	case 'e':
	case 'i':
	case 'o':
	case 'u':
		++vowel;
		break;
	case 'w':
	case 'y':
		++semivowel;
	default:
		++consonant;
		break;
}
```

## problem 2 (4 points)

__answer__

```console
101#1
```

## problem 3 (7 points)

### (a) (3 points)

__answer__

```Cpp
int pre_increment(int &x) {
	x += 1;
	return x;
}
```

### (b) (4 points)

__answer__

```Cpp
int post_increment(int &x) {
	int pre{x};
	x += 1;
	return pre;
}
```

## problem 4 (6 points)

__answer__

1. `int&`
2. `int`

## problem 5 (6 points)

### (a) (3 points)

__anwswer__

`print_user_sum` has two overloads `void print_user_sum(double x, int y, char user)` and `void print_user_sum(int x, double y, char user)`. However, the code calling it `print_user_sum(0.5, -0.5, 'A');` passes two `double`s as the first two arguments, which matches none of the two overloads as `double`s cannot be implicitly converted into `int`s. So there will be a compilation error in the code calling `print_user_sum`. To fix it, add an additional overload (with the definition) with a signature of `void print_user_sum(double x, double y, char user)`.

### (b) (3 points)

__answer__

`mystery` has an overload with a signature `void mystery(double x, int y = 0, char z)`, which is illegal in C++ because default parameter(s) (`int y = 0`) cannot be followed by non-default parameters (`char z`), so an compilation error occurs there. To fix it, remove that one overload along with the definition since the code calling `mystery` `mystery(0.5, '*');` only uses the remaining overload `void mystery(double x, char y)` anyway.

## problem 6 (13 points)

__answer__

```Cpp
void hat(int height) {
	for (int yy{0}; yy < height; ++yy) {
		int left{height - yy - 1}, right{height + yy - 1};
		for (int xx{0}; xx < (height * 2 - 1); ++xx) {
			if (xx == left || xx == right) {
				cout << '*';
				continue;
			}
			cout << '#';
		}
		cout << endl;
	}
}
```

## problem 7 (12 points)

> - `size = 11`
> - `i` from 1 to end of array `a`
> 	- check if `a[0]` to `a[k]` is all different from `a[i]`
> 		- if so, increment `k` and set `a[k]` to `a[i]`
>
> 1. `i = 1, k = 1`
> 2. `i = 2, k = 2`
> 3. `i = 3, k = 2`
> 4. `i = 4, k = 3, a[3] = 70`
> 5. `i = 5, k = 3`
> 6. `i = 6, k = 3`
> 7. `i = 7, k = 3`
> 8. `i = 8, k = 3`
> 9. `i = 9, k = 3`
> 10. `i = 10, k = 4, a[4] = 66`
> 11. `size = n = 5, arr = {58, 26, 91, 70, 66, 70, 91, 58, 58, 58, 66}`
> 12. `cout << "58 26 91 70 66 size = 5"`

__answer__

```console
58 26 91 70 66 size = 5
```

## problem 8 (14 points)

### (a) (6 points)

__answer__

```Cpp
int array_max(int array[], int length) {
	if (length == 1) { return array[0]; }
	int max{array_max(array, length - 1)};
	if (array[length - 1] > max) {
		return array[length - 1];
	}
	return max;
}
```

### (b) (8 points)

__answer__

```Cpp
int matrix_max(int array[][8], int rows, int cols) {
	if (rows == 1) { return array_max(array[0], cols); }
	int max{matrix_max(array, rows - 1, cols)};
	if (array_max(array[rows - 1], cols) > max) {
		return array_max(array[rows - 1]);
	}
	return max;
}
```

## problem 9 (28 points)

### (a) (4 points)

__answer__

```Cpp
bool same_word(const char a[], const char b[]) {
	int ii{0};
	for (; a[ii] != '\0' && b[ii] != '\0'; ++ii) {
		if (a[ii] != b[ii]) {
			return false;
		}
	}
	return a[ii] == b[ii];
}
```

### (b) (10 points)

__answer__

```Cpp
int get_words_from_sentence(char const sentence[], char (*words)[WORD_LEN + 1]) {
	int curWord{0}, chars{0};
	for (int ii{0}; sentence[ii] != PERIOD; ++ii) {
		if (sentence[ii] == SPACE) {
			words[curWord][chars] = '\0';
			++curWord;
			chars = 0;
			continue;
		}
		words[curWord][chars] = sentence[ii];
		++chars;
	}
	if (sentence[0] == PERIOD) { return 0; }
	words[curWord][chars] = '\0';
	return curWord + 1;
}
```

### (c) (10 points)

__answer__

```Cpp
int spell_check(char const (*dict)[WORD_LEN + 1], int dict_size, char const (*words)[WORD_LEN + 1], int num_words, int found_words_index[]) {
	int found{0};
	for (int ww{0}; ww < num_words; ++ww) {
		for (int dd{0}; dd < dict_size; ++dd) {
			if (same_word(words[ww], dict[dd])) {
				found_words_index[found] = ww;
				++found;
				break;
			}
		}
	}
	return found;
}
```

### (d) (4 points)

__answer__

```Cpp
void print_found_words(char const (*words)[WORD_LEN + 1], int const found_words_index[], int num_words_found) {
	for (int ii{0}; ii < num_words_found; ++ii) {
		char const *word{words[found_words_index[ii]]};
		cout << "word " << ii << " : " << word << endl;
	}
}
```
