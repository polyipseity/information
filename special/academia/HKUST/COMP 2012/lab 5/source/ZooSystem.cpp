#include "ZooSystem.h"
#include "Animal.h"

ZooSystem::ZooSystem(int cap) : animals{new Animal*[cap]}, capacity(cap), size(0){
// To do4: Implement the ZooSystem constructor
}

ZooSystem::~ZooSystem()
{
    for (decltype(size) idx{}; idx < size; ++idx)
        delete animals[idx];
    delete[] animals;
}

void ZooSystem::addAnimal(Animal* animal) {
// To do4: Implement the addAnimal function
if (size < capacity) {
// Check if array is full
// Add animal to array
animals[size++] = animal;
} else {
// Handle array being full, maybe resize or ignore
cout << "Array is full, unable to add animal.\n";
}
}

void ZooSystem::listAllAnimals() const {
// To do4: Implement the listAllAnimals function
    for (decltype(size) idx{}; idx < size; ++idx)
        animals[idx]->describe();
}

void ZooSystem::listCarnivores() const {
// To do4: Implement the listCarnivores function
    for (decltype(size) idx{}; idx < size; ++idx)
    {
        if (animals[idx]->getFoodType() == FoodType::Meat)
            animals[idx]->describe();
    }
}

void ZooSystem::listHerbivores() const {
// To do4: Implement the listHerbivores function
    for (decltype(size) idx{}; idx < size; ++idx)
    {
        if (animals[idx]->getFoodType() == FoodType::Vegetable)
            animals[idx]->describe();
    }
}


double ZooSystem::calculateMeatConsumption() const {
// Todo4: Implement the calculateMeatConsumption function
    double totalMeatConsumption{};
    for (decltype(size) idx{}; idx < size; ++idx)
    {
        if (animals[idx]->getFoodType() == FoodType::Meat)
            totalMeatConsumption += animals[idx]->getFoodPerDay();
    }
    return totalMeatConsumption;
}

double ZooSystem::calculateVegetableConsumption() const {
// Todo4: Implement the calculateVegetableConsumption function
    double totalVegetableConsumption{};
    for (decltype(size) idx{}; idx < size; ++idx)
    {
        if (animals[idx]->getFoodType() == FoodType::Vegetable)
            totalVegetableConsumption += animals[idx]->getFoodPerDay();
    }
    return totalVegetableConsumption;
}

