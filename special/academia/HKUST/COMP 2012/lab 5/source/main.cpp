#include "ZooSystem.h"
#include "SpecificAnimal.h"
#include <iostream>


using namespace std;

int main() {
    ZooSystem zoo(50);
    
    zoo.addAnimal(new Lion("Simba", 5, 5.0, 20));
    zoo.addAnimal(new Elephant("Dumbo", 10, 50.0, "Grass", "Savanna"));
   
    // list all animals in the zoo
    cout << "All animals in the zoo:" << endl;
    zoo.listAllAnimals();

    // list all carnivores in the zoo
    cout << "Carnivores in the zoo:" << endl;
    zoo.listCarnivores();

    // list all herbivores in the zoo
    cout << "Herbivores in the zoo:" << endl;
    zoo.listHerbivores();

    // calculate total food consumption per day
    cout << "Total meat consumption per day: " << zoo.calculateMeatConsumption() << " kg" << endl;
    cout << "Total vegetable consumption per day: " << zoo.calculateVegetableConsumption() << " kg" << endl;

    return 0;
}
