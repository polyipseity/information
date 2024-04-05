#include "Animal.h"
#include <iostream>

using namespace std;



Animal::Animal() {
    // Todo 1: Implement the Animal constructor
}



Carnivore::Carnivore() {
    // Todo 2.1: Implement the Carnivore constructor
}



Herbivore::Herbivore() {
    // Todo 2.2: Implement the Herbivore constructor
}


// describe implementations
void Carnivore::describe() const {
    cout << "Carnivore: " << name << ", Age: " << age
              << ", Consumes " << getFoodPerDay() << " kg of meat per day." 
              << " Teeth Count: " << teethCount << endl;
}

void Herbivore::describe() const {
    cout << "Herbivore: " << name << ", Age: " << age
              << ", Consumes " << getFoodPerDay() << " kg of vegetation per day." 
              << " Favorite Plant: " << favoritePlant
              << ", Habitat Preference: " << habitatPreference << endl;
}
