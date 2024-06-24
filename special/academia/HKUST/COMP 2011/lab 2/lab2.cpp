#include <iostream>
using namespace std;

int main()
{
    int number1, number2; // Both inputs will be positive integers, but you do not know which is larger
    int small, large;     // small should be the smaller of the two numbers, large should be the larger
    int finalScore = 0;   // The final score of the game

    // Get the range from the user
    cin >> number1 >> number2;

    /* Please do not change the code above this line */

    // Task 1 - Find the small and large bounds of the range
    if (number1 > number2)
    {
        large = number1;
        small = number2;
    }
    else
    {
        large = number2;
        small = number1;
    }

    // Task 2 - Find the perfect numbers in the range and update the final score
    for (int cur{small}; cur <= large; ++cur)
    {
        int sum{0};
        for (int div{1}; div <= cur / 2; ++div)
        {
            if (cur % div == 0)
            {
                sum += div;
            }
        }
        finalScore += cur * (cur == sum ? 1 : -1);
    }

    /* Please do not change the code below this line */

    cout << finalScore;
    return 0;
}