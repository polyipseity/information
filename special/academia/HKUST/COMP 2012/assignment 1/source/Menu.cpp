#include "Menu.h"

// Task 3.1
Menu::Menu() : foodItems{new Food[10]}, currentSize{}, capacity{10}, nextFoodId{1} {
}

// Task 3.2
Menu::~Menu() {
    delete[] foodItems;
}

// Task 3.3
void Menu::addFood(const Food& food) {
    if (currentSize >= capacity)
    {
        resizeArray();
    }
    Food &my_food{foodItems[currentSize++]};
    my_food = food;
    my_food.setFoodId(nextFoodId++);
}

// Task 3.4
bool Menu::removeFood(int id) {
    int foundIdx{findFoodIndex(id)};
    if (foundIdx == -1)
        return false;
    --currentSize;
    for (int idx{foundIdx}; idx < currentSize; ++idx)
        foodItems[idx] = foodItems[idx + 1];
    return true;
}

// Task 3.5
int Menu::findFoodIndex(int id) const {
    for (int idx{}; idx < currentSize; ++idx)
    {
        if (foodItems[idx].getFoodId() == id)
            return idx;
    }
    return -1;
}

// Task 3.6
const Food* Menu::getFoodById(int id) const {
    int foundIdx{findFoodIndex(id)};
    return foundIdx == -1 ? nullptr : &foodItems[foundIdx];
}

// Task 3.7
void Menu::resizeArray() {
    Food *const newFoodItems{new Food[capacity * 2]};
    for (int idx{}; idx < currentSize; ++idx)
    {
        newFoodItems[idx] = foodItems[idx];
    }
    delete[] foodItems;
    foodItems = newFoodItems;
    capacity *= 2;
}

// ---------------------- provided functions: DO NOT MODIFY --------------------------
void Menu::displayMenu() const {
    if (currentSize == 0) {
        cout << "Menu is empty." << endl;
        return;
    }
    for (int i = 0; i < currentSize; i++) {
        cout << "ID: " << foodItems[i].getFoodId() << ", Name: " << foodItems[i].getFoodName() << ", Price: $" << foodItems[i].getPrice() << endl;
    }
}

void Menu::manageFoodItems() {
    int choice, id;

    do {
        // Display options
        cout << "\n** Manage Food Items **\n";
        cout << "1. Add food item\n";
        cout << "2. Update food price\n";
        cout << "3. Remove food item\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";

        cin >> choice;

        switch (choice) {
            case 1: {
                cout << "Current Menu items: "<< endl;
                displayMenu();
                if (isFull()) {
                    cout << "Menu is full. Cannot add more food items." << endl;
                    return;
                }
                    // Get user input for food details
                    string name;
                    float price; // Ensure this is float to match the constructor

                    cout << "Enter food name: ";
                    cin >> name;

                    cout << "Enter food price: ";
                    cin >> price;
                    Food newFood(nextFoodId, name, price); // Use nextFoodId here
                    addFood(newFood);
                    cout << "Food item added successfully." << endl;
                break;
            }
            case 2: {
                cout << "Current Menu items: "<< endl;
                displayMenu();
                cout << "Enter the ID of the food item to update: ";
                cin >> id;
                int index = findFoodIndex(id); // Scope introduced for index
                if (index == -1) {
                    cout << "Food item with ID " << id << " not found." << endl;
                    break;
                }
                double newPrice;
                cout << "Enter the new price: ";
                cin >> newPrice;
                foodItems[index].setPrice(newPrice);
                cout << "Price updated successfully." << endl;
                break;
            }
            case 3: {
                cout << "Current Menu items: "<< endl;
                displayMenu();
                cout << "Enter the ID of the food item to remove: ";
                cin >> id;
                if (removeFood(id)) {
                    cout << "Food item removed successfully." << endl;
                }
                break;
            }
            case 4: {
                cout << "Exiting food item management." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
                break;
            }
        }
    } while (choice != 4);
}