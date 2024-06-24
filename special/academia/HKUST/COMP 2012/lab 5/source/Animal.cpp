#include "Animal.h"
#include <iostream>

using namespace std;



Animal::Animal(string const &name, int age, double foodPerDay, FoodType foodType)
    : name{name}, age{age}, foodPerDay{foodPerDay}, foodType{foodType} {
    // Todo 1: Implement the Animal constructor
}



Carnivore::Carnivore(string const &name, int age, double foodPerDay, int teethCount)
    : Animal{name, age, foodPerDay, FoodType::Meat}, teethCount{teethCount} {
    // Todo 2.1: Implement the Carnivore constructor
}



Herbivore::Herbivore(string const &name, int age, double foodPerDay, string const &favoritePlant, string const &habitatPreference)
    : Animal{name, age, foodPerDay, FoodType::Vegetable}, favoritePlant{favoritePlant}, habitatPreference{habitatPreference} {
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
