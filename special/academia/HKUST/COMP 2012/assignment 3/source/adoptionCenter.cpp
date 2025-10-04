#include "adoptionCenter.h"
#include <iostream>
using namespace std;


// TASK 4.1: AdoptionCenter constructor
// Initialize all data members to represent an empty database.
// The BSTs need to be initialized with their comparison functions:
// - NAME: Sort by species name (including breed), in increasing lexicographic order
// - AGE: Sort by increasing age
// - HEALTH: Sort by increasing health severity
// - VACCINE: Sort by increasing VaccinationStatus total hash value
//
// The comparison functions when comparing the left animal (a1) and right animal (a2) should return:
// - a negative value if a1 < a2
// - 0 if a1 == a2
// - a positive value if a1 > a2
//
// Hints:
// - You can write lambda functions to pass into the BST constructors
// - For comparing strings, look up the documentation for std::string::compare()
// - Be careful when performing arithmetic calculations with unsigned int
AdoptionCenter::AdoptionCenter()
    : animals{}, numAnimals{}, sortedAnimals{
                                   BST{[](Animal const *left, Animal const *right)
                                       {
                                           return left->getSpecies() < right->getSpecies() ? -1 : left->getSpecies() > right->getSpecies() ? 1
                                                                                                                                           : 0;
                                       }},
                                   BST{[](Animal const *left, Animal const *right)
                                       {
                                           return left->getAge() < right->getAge() ? -1 : left->getAge() > right->getAge() ? 1
                                                                                                                           : 0;
                                       }},
                                   BST{[](Animal const *left, Animal const *right)
                                       {
                                           return left->getHealthCondition().severity < right->getHealthCondition().severity ? -1 : left->getHealthCondition().severity > right->getHealthCondition().severity ? 1
                                                                                                                                                                                                               : 0;
                                       }},
                                   BST{[](Animal const *left, Animal const *right)
                                       {
                                           return left->getVaccinationStatus().getTotalHashValue() < right->getVaccinationStatus().getTotalHashValue() ? -1 : left->getVaccinationStatus().getTotalHashValue() > right->getVaccinationStatus().getTotalHashValue() ? 1
                                                                                                                                                                                                                                                                   : 0;
                                       }},
                               } {

    // TODO

}

// TASK 4.2: AdoptionCenter destructor
// Deallocate any dynamic memory in this class.
// Hint: This is where the animals should be deallocated.
AdoptionCenter::~AdoptionCenter() {

    // TODO
    for (unsigned int idx{}; idx < numAnimals; ++idx)
        delete animals[idx];
    delete[] animals;
}

// TASK 4.3: AdoptionCenter::addAnimal(Animal*)
// Add an animal to the dynamic-length array data member,
// by increasing its size by 1 and increment numAnimals accordingly.
// Add the animal to the end of the array,
// such that the array is sorted by increasing ID (assume we only add increasing IDs)
// The animal should also be added to the 4 BSTs.
void AdoptionCenter::addAnimal(Animal* a) {

    // TODO
    Animal **newAnimals{new Animal*[numAnimals + 1]};
    if (animals)
    {
        for (unsigned int idx{}; idx < numAnimals; ++idx)
            newAnimals[idx] = animals[idx];
    }
    delete[] animals;
    animals = newAnimals;
    newAnimals[numAnimals++] = a;
    for (unsigned int idx{}; idx < sizeof(sortedAnimals) / sizeof(*sortedAnimals); ++idx)
        sortedAnimals[idx].insert(a);
}

// TASK 4.4: AdoptionCenter::removeAnimal(unsigned int)
// Remove an animal from the database by ID.
// If the ID does not exist, do nothing.
// Otherwise, resize the array to decrease its size by 1,
// copy the non-deleted animals over and decrement numAnimals accordingly.
// The animal should also be removed from the 4 BSTs.
// Finally, return true if the animal was successfully removed.
bool AdoptionCenter::removeAnimal(unsigned int id) {

    // TODO
    for (unsigned int idx{}; idx < numAnimals; ++idx)
    {
        Animal *animal{animals[idx]};
        if (animal->getID() == id)
        {
            Animal **newAnimals{new Animal*[numAnimals - 1]};
            for (unsigned int idx2{}, new_idx{}; idx2 < numAnimals; ++idx2)
            {
                if (idx2 == idx)
                    continue;
                newAnimals[new_idx++] = animals[idx2];
            }
            --numAnimals;
            delete[] animals;
            animals = newAnimals;
            if (numAnimals <= 0)
            {
                delete[] animals;
                animals = nullptr;
            }
            for (unsigned int idx2{}; idx2 < sizeof(sortedAnimals) / sizeof(*sortedAnimals); ++idx2)
                sortedAnimals[idx2].remove(animal);
            delete animal;
            return true;
        }
    }
    return false;
}

// TASK 4.5: AdoptionCenter::incrementAge()
// Increment the age of all animals by 1.
void AdoptionCenter::incrementAge()
{

    // TODO
    for (unsigned int idx{}; idx < numAnimals; ++idx)
        animals[idx]->incrementAge();
}

// TASK 4.6: AdoptionCenter::setAnimalHealthCondition(unsigned int, const HealthCondition&)
// Modify the animal with the specified ID's health condition to the provided parameter.
// If the animal does not exist, do nothing.
// Else, ensure the BST for health condition is sorted after the modification.
void AdoptionCenter::setAnimalHealthCondition(unsigned int id, const HealthCondition& h)
{

    // TODO
    for (unsigned int idx{}; idx < numAnimals; ++idx)
    {
        if (animals[idx]->getID() != id)
            continue;
        sortedAnimals[SortCriteria::HEALTH].remove(animals[idx]);
        animals[idx]->setHealthCondition(h);
        sortedAnimals[SortCriteria::HEALTH].insert(animals[idx]);
        break;
    }
}

// TASK 4.7: AdoptionCenter:addAnimalVaccine(unsigned int, const string&)
// Add the provided vaccine to the animal specified by ID.
// If the animal does not exist, do nothing.
// Else, ensure the BST for vaccine status is sorted after the modification.
void AdoptionCenter::addAnimalVaccine(unsigned int id, const string& v)
{

    // TODO
    for (unsigned int idx{}; idx < numAnimals; ++idx)
    {
        if (animals[idx]->getID() != id)
            continue;
        sortedAnimals[SortCriteria::VACCINE].remove(animals[idx]);
        animals[idx]->addVaccine(v);
        sortedAnimals[SortCriteria::VACCINE].insert(animals[idx]);
        break;
    }
}

// TASK 4.8: AdoptionCenter::setAnimalSpecialNeeds(unsigned int, const std::string&)
// Modify the animal with the specified ID's special needs to the provided parameter.
// If the animal does not exist, do nothing.
void AdoptionCenter::setAnimalSpecialNeeds(unsigned int id, const std::string& n)
{

    // TODO
    for (unsigned int idx{}; idx < numAnimals; ++idx)
    {
        if (animals[idx]->getID() != id)
            continue;
        animals[idx]->setSpecialNeeds(n);
        break;
    }
}


/**
 * Provided function to display the animals in the database.
 * @param start: Starting index to print (e.g. start == 5: ignore the first 5 animals that matches the filter)
 * @param stop: Index to stop printing (e.g. stop == 10: print until the 10th animal [exclusive] that matches the filter)
 * @param filter: Only print animals that match this filter.
 * @param criteria: Sorting criteria. By default sort by ID (assuming animals are added in increasing ID)
*/
void AdoptionCenter::display(unsigned int start, unsigned int stop, const Filter& filter, SortCriteria criteria) const {
    unsigned int displayCount = stop - start;
    if (criteria == ID) {
        for (unsigned int i=0; i<numAnimals; ++i) {
            if (filter.match(*animals[i])) {
                animals[i]->display(start, displayCount);
            }
        }
    }
    else {
        sortedAnimals[criteria].print(start, displayCount, filter);
    }
}

/**
 * Provided function to print the vaccines an animal, specified by ID, has taken.
*/
void AdoptionCenter::displayPetVaccines(unsigned int id) const
{
    unsigned int i = 0;
    for (; i<numAnimals; ++i) {
        if (animals[i]->getID() == id) {
            VaccinationStatus v = animals[i]->getVaccinationStatus();
            if (v.numVaccines == 0)
                cout << "No vaccines found." << endl;
            else
                for (unsigned int j = 0; j < VACCINE_TABLE_SIZE; ++j) {
                    if (v.vaccineHashTable[j].length() > 0)
                        cout << v.vaccineHashTable[j] << endl;
                }
            return;
        }
    }
    if (i == numAnimals)
        cout << "ID not found in database." << endl;
}
