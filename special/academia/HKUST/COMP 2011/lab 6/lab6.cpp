/* 
 * File: lab6_skeleton.cpp
 *
 * Lab 6: Recursion - Alien Word Parsing
 */

#include <iostream>
#include <cstring>

using namespace std;

const int MAX_LEN = 256; 

bool correct_word(char const string[], int begin, int end)
{
    

   /* ADD YOUR CODE HERE */
   /* THIS MUST BE A RECURSIVE FUNCTION */
   if (begin < 0 || begin > end)
      return false;
    // Task 1: Base case with only a single character
   if (begin == end && 'a' <= string[begin] && string[begin] <= 'z')
      return true;
    // Task 2: Recursive case with suffix characters '@', or '#'
   if (string[end] == '@' || string[end] == '#')
      return correct_word(string, begin, end - 1);
    // Task 3: Recursive case with concatenation characters '|' at suffix position.
   if (string[end] == '|')
   {
      for (int ii{begin}; ii <= end - 2; ++ii)
      {
         if (correct_word(string, begin, ii) && correct_word(string, ii + 1, end - 1))
            return true;
      }
   }
    // Task 4: Recursive case with concatenation characters '#' at prefix position.
   if (string[begin] == '#')
   {
      for (int ii{begin + 1}; ii <= end - 1; ++ii)
      {
         if (correct_word(string, begin + 1, ii) && correct_word(string, ii + 1, end))
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
   } while (c == 'Y' || c=='y');

   return 0;
}

