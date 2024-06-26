#ifndef ZOOSYSTEM_H
#define ZOOSYSTEM_H

#include "Animal.h"

class ZooSystem {
private:
    Animal** animals; // Dynamic array of pointers to Animal
    int capacity;     // Capacity of the array
    int size;         // Current number of animals in the array

public:
    ZooSystem(int cap);
    ~ZooSystem();

    void addAnimal(Animal* animal);
    void listAllAnimals() const;
    void listCarnivores() const;
    void listHerbivores() const;
    double calculateMeatConsumption() const;
    double calculateVegetableConsumption() const;
};

#endif // ZOOSYSTEM_H
