#include "ZooSystem.h"
#include "Animal.h"

ZooSystem::ZooSystem(int cap) : capacity(cap), size(0){
// To do4: Implement the ZooSystem constructor
}

void ZooSystem::addAnimal(Animal* animal) {
// To do4: Implement the addAnimal function
if ( ) {
// Check if array is full
// Add animal to array
} else {
// Handle array being full, maybe resize or ignore
cout << "Array is full, unable to add animal.\n";
}
}

void ZooSystem::listAllAnimals() const {
// To do4: Implement the listAllAnimals function
}

void ZooSystem::listCarnivores() const {
// To do4: Implement the listCarnivores function
}

void ZooSystem::listHerbivores() const {
// To do4: Implement the listHerbivores function
}


double ZooSystem::calculateMeatConsumption() const {
// Todo4: Implement the calculateMeatConsumption function
    return totalMeatConsumption;
}

double ZooSystem::calculateVegetableConsumption() const {
// Todo4: Implement the calculateVegetableConsumption function
    return totalVegetableConsumption;
}

