#ifndef MENU_H
#define MENU_H

#include "Food.h"
#include <iostream>
#include <string>
using namespace std;

class Menu {
private:
    Food* foodItems; // Dynamic array of food items
    int currentSize; // Current number of food items
    int capacity; // Maximum capacity of the array
    int nextFoodId; //Track the next available food item ID
    
public:
    Menu(); // Constructor to initialize currentSize and allocate memory for foodItems
    ~Menu(); // Destructor to free allocated memory
    void addFood(const Food& food);
    bool removeFood(int id);
    void displayMenu() const;
    void manageFoodItems();
    const Food* getFoodById(int id) const;

private: //Helper Functions
    bool isFull() const { return currentSize == capacity; }
    void resizeArray(); // Resizes the array if needed
    int findFoodIndex(int id) const;
};

#endif // MENU_H
