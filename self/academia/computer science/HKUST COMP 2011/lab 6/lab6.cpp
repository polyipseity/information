/* 
 * File: lab6_skeleton.cpp
 *
 * Lab 6: Recursion - Alien Word Parsing
 */

#include <iostream>
#include <cstring>

using namespace std;

const int MAX_LEN = 256; 

/* ADD THE RETURN TYPE HERE */ correct_word(/* ADD FORMAL PARAMETER LIST HERE */)
{
    
   /* ADD YOUR CODE HERE */
   /* THIS MUST BE A RECURSIVE FUNCTION */

    // Task 1: Base case with only a single character

    // Task 2: Recursive case with suffix characters '@', or '#'

    // Task 3: Recursive case with concatenation characters '|' at suffix position.

    // Task 4: Recursive case with concatenation characters '#' at prefix position.

    // All remaining cases are wrong
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

