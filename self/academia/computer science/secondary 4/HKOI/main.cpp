#include <string>
#include <iostream>

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
        } /* add additional tasks here, should use an 'unordered_map' */ else {
            cerr << "Task not found: " << choice << endl;
            choose = true;
        }
    } while (choose);

    return result;
}
