#include <iostream>

using namespace std;

const int MAX_RADAR_CAPACITY = 5;

// Task 1: Initialize the radar system
void initialize_radar_system(int radar[]) {
    for (int i = 0; i < MAX_RADAR_CAPACITY; i++) {
        radar[i] = 0; // Initialize all radar elements to 0 (no alien detected).
    }
}

// Task 2: Detect and track an incoming alien ship
// tips: if radar is marked as 0, it means no alien ship is detected, so we can track it.
bool detect_alien_ship(int radar[], int alienID) {
    // Check if radar is already full
    for (int i = 0; i < MAX_RADAR_CAPACITY; i++) {
        if (radar[i] == 0) {
            radar[i] = alienID; // Track the alien ship
            return true; // Alien ship detected and tracked successfully
        }
    }
    return false; // Radar is already full, cannot track more aliens
}

// Task 3: Engage in battle and eliminate all alien ships with a specific ID
// tips: set eliminated alien ships to 0, no need to remove them from the array.
int engage_in_battle(int radar[], int alienID) {
    int count = 0; // Initialize count of eliminated alien ships to 0
    for (int i = 0; i < MAX_RADAR_CAPACITY; i++) {
        if (radar[i] == alienID) {
            radar[i] = 0; // Eliminate the alien ship
            count++; // Increment the count of eliminated alien ships
        }
    }
    return count; // Return the total count of eliminated alien ships
}

// Task 4: Count the total number of alien ships currently in radar
int count_total_alien_ships(int radar[]) {
    int count = 0; // Initialize count to 0
    for (int i = 0; i < MAX_RADAR_CAPACITY; i++) {
        if (radar[i] != 0) {
            count++; // Increment count for each detected alien ship
        }
    }
    return count; // Return the total count of detected alien ships
}

// Task 5: Display the current radar status
// tips: you need to display the radar status in the following format:
//      Radar Status: [1 1 1 0 0]
void display_radar_status(int radar[]) {
    cout << "Radar Status: [";
    for (int i = 0; i < MAX_RADAR_CAPACITY; i++) {
        cout << radar[i];
        if (i < MAX_RADAR_CAPACITY - 1) {
            cout << " ";
        }
    }
    cout << "]" << endl;
}

int main() {
    int radar[MAX_RADAR_CAPACITY];
    initialize_radar_system(radar);
    cout << "Alien Invasion Game Menu:" << endl;
    cout << "1. Detect and track an alien ship" << endl;
    cout << "2. Engage in battle and eliminate alien ships" << endl;
    cout << "3. Count total alien ships" << endl;
    cout << "4. Display radar status" << endl;
    cout << "0. Quit the game" << endl;
    int choice;
    do {
        cout << "Enter your choice: ";
        cin >> choice;

        int alienID;
        int eliminatedCount;
        int totalAlienShips;

        switch (choice) {
            case 1:
                cout << "Enter the ID of the alien ship to detect: ";
                cin >> alienID;
                if (detect_alien_ship(radar, alienID)) {
                    cout << "Alien ship with ID " << alienID << " detected and tracked." << endl;
                } else {
                    cout << "Radar is already full. Cannot track more aliens." << endl;
                }
                break;
            case 2:
                cout << "Enter the ID of the alien ship to engage in battle: ";
                cin >> alienID;
                eliminatedCount = engage_in_battle(radar, alienID);
                cout << "Eliminated " << eliminatedCount << " alien ship(s) with ID " << alienID << "." << endl;
                break;
            case 3:
                totalAlienShips = count_total_alien_ships(radar);
                cout << "Total number of detected alien ships: " << totalAlienShips << endl;
                break;
            case 4:
                display_radar_status(radar);
                break;
            case 0:
                cout << "Exiting the game. Goodbye!";
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }

    } while (choice != 0);

    return 0;
}

