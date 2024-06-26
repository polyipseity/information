#ifndef __ADOPTIONCENTER_H__
#define __ADOPTIONCENTER_H__

#include "animal.h"
#include "bst.h"

/**
 * An enum for animal sorting criteria
 * Can be used as index into the BST array,
 * i.e. sortedAnimals[AGE] is the BST sorted by AGE
*/
enum SortCriteria {
    NAME,
    AGE,
    HEALTH,
    VACCINE,
    ID // equals to number of criterias
};

/**
 * Class representing the adoption center database.
 * Contains a dynamic-length array of Animals,
 * and 4 BSTs for the 4 sorting criterias other than ID.
 * 
 * These data members should be modified accordingly whenever an Animal is inserted, removed, or modified.
*/
class AdoptionCenter {
    private:
        // Dynamic-length array of dynamic-allocated animals.
        // The size of the array is equal to the number of animals.
        // New animals should be added to the end of the array.
        Animal** animals;
        unsigned int numAnimals;

        // Array of BST data members to sort the animals as they are added/removed/modified
        BST sortedAnimals[ID];

    public:
        // Default constructor, initializes an empty database
        AdoptionCenter();

        // Copy constructor and assignment operator are deleted
        AdoptionCenter(const AdoptionCenter&) = delete;
        AdoptionCenter& operator=(const AdoptionCenter&) = delete;

        // Destructor
        ~AdoptionCenter();

        // Add an animal
        void addAnimal(Animal* a);
        // Remove an animal by ID
        bool removeAnimal(unsigned int id);

        // Functions to modify existing animal(s)
        // The relevant BSTs should be updated accordingly
        void incrementAge();
        void setAnimalHealthCondition(unsigned int id, const HealthCondition& h);
        void addAnimalVaccine(unsigned int id, const std::string& v);
        void setAnimalSpecialNeeds(unsigned int id, const std::string& n);
        
        // Display a page of animals that match the filter in the chosen sorting criteria
        void display(unsigned int start, unsigned int stop, const Filter& filter, SortCriteria criteria = ID) const;

        // Display the vaccines a pet has taken
        void displayPetVaccines(unsigned int id) const;
};

#endif // __ADOPTIONCENTER_H__