#include <iostream>
#include <cstring>
using namespace std;
const int MAX_LEN = 256;

bool correct_word(const char word[], int i, int j)
{
    // This shouldn't happen
    if (j < i)
        return false;

    char c = word[j];

    // Base case with only a single character
    if (i == j)
        return ( c>='a' && c<='z');

    // Recursive case with suffix characters '*' or '#'
    if (c == '#' || c == '@')
        return correct_word(word, i, j-1);

    // Recursive case with concatenation characters '|' at suffix position
    if (c == '|')
    {
        for (int k = i; k < j-1; k++)
        {
            if (correct_word(word, i, k) && correct_word(word, k+1, j-1))
                return true;
        }

        return false;
    }

    // Recursive case with concatenation characters '|' at prefix position
    c = word[i];
    if (c == '#'){
        for (int k = i+1; k < j; k++)
        {
            if (correct_word(word, i+1, k) && correct_word(word, k+1, j))
                return true;
        }
    }


    // All remaining cases are wrong
    return false;
}


int main()
{
   char word[MAX_LEN];
   char c;

   do{
      cout << "Enter a word: ";
      cin >> word;
      if (correct_word(word, 0, strlen(word) - 1))
         cout << "The word is CORRECT!\n";
      else
         cout << "The word is INCORRECT!\n";
      cout << "Do you want to enter a new word ('Y'/'y' for Yes, 'N'/'n' for No)? ";
      cin >> c;
   } while(c == 'Y' || c=='y');


   return 0;
}

