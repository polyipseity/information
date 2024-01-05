#include <iostream>
using namespace std;

int main() {
    int number1, number2; // Both inputs will be positive integers, but you do not know which is larger
    int small, large; // small should be the smaller of the two numbers, large should be the larger
    int finalScore = 0; // The final score of the game

    // Get the range from the user
    cin >> number1 >> number2;

    /* Please do not change the code above this line */ 

    // Task 1 - Find the small and large bounds of the range
    ///////////////////
    // Your Code Here //
    ///////////////////
    small = number1 < number2 ? number1 : number2;
    large = number1 > number2 ? number1 : number2; 

    

    // Task 2 - Find the perfect numbers in the range and update the final score
    for (int num = small; num <= large; ++num) {
        ///////////////////
        // Your Code Here //
        ///////////////////
        int sum = 0;

        // Find the divisors of the number
        for (int i = 1; i <= num / 2; ++i) {
            if (num % i == 0) {
                sum += i;
            }
        }

        // Check if the number is perfect
        // Print the number if it is perfect
        if (sum == num) {
            finalScore += num;
        } else {
            finalScore -= num;
        }

    }

    /* Please do not change the code below this line */
    
    cout << finalScore;
    return 0;
}