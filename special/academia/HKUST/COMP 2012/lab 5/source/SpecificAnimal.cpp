#include "SpecificAnimal.h"   
#include <iostream>
using namespace std;

Lion::Lion(const string& name, int age, double foodPerDay, int teethCount)
    : Carnivore(name, age, foodPerDay, teethCount) {}

void Lion::describe() const {
    cout << "Lion: " << name << " is " << age << " years old and eats " << foodPerDay << "kg of meat per day." 
         << ", Teeth Count: " << getTeethCount() << endl;
}

// Tiger class


// Todo 3.1: Implement the Tiger class according to the Lion class and the sample output.





// Elephant class

// Todo 3.2: Implement the Elephant class according to the Lion class and the sample output. 