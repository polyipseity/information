#include <string>
#include <iostream>
#include "S191/unstoppable_onslaught.h"

using namespace std;

int main(int const argc, char *const *const argv) noexcept {
    int result; // will eventually be set

    bool choose;
    do {
        choose = false;
        
        string choice;
        cout << "Choose a task: ";
        getline(cin, choice);

        // I heard you like giant if statements, no?
        if (choice.empty()) {
            cout << "No tasks selected." << endl;
            result = 0;
        } else if (choice == "s191")
            result = s191::main(argc, argv);
        else {
            cerr << "Task not found: " << choice << endl;
            choose = true;
        }
    } while (choose);

    return result;
}
