#ifndef __ANIMAL_H__
#define __ANIMAL_H__

#include <iostream>
#include "datatypes.h"

/**
 * Class representing an animal and its attributes.
*/
class Animal {
    private:
        // Data members: ID, Species (breed), Age, Health condition, Vaccine status, Special needs
        unsigned int id;
        Species species;
        unsigned int age;

        HealthCondition healthCondition;
        VaccinationStatus vaccineStatus;
        
        std::string specialNeeds;
    
    public:
        // Constructor
        Animal(
            unsigned int id, const Species& s, unsigned int a, 
            const HealthCondition& h = NORMAL_HEALTH,
            const VaccinationStatus& v = VaccinationStatus(),
            const std::string& n = ""
        ): id(id), species(s), age(a), healthCondition(h), vaccineStatus(v), specialNeeds(n) {}

        // Copy constructor and assignment operator are deleted
        Animal(const Animal&) = delete;
        Animal& operator=(const Animal&) = delete;

        // Accessor functions
        unsigned int getID() const { return id; }
        std::string getSpecies() const { return species.name + " (" + species.breed + ")"; }
        unsigned int getAge() const { return age; }
        const HealthCondition& getHealthCondition() const { return healthCondition; }
        const VaccinationStatus& getVaccinationStatus() const { return vaccineStatus; }
        std::string getSpecialNeeds() const { return specialNeeds; }

        // Mutator functions
        void incrementAge() { ++age; }
        void setHealthCondition(const HealthCondition& h) { healthCondition = h; }
        void setSpecialNeeds(const std::string& n) { specialNeeds = n; }
        void addVaccine(const std::string& v) { vaccineStatus.addVaccine(v); }

        // Display the animal, depending on the counters
        // If ignoreCount > 0, decrement it without printing.
        // Else, print and decrement displayCount, unless it equals 0.
        //
        // E.g.:
        // - display(2, 2) -> does not print
        // - display(0, 2) -> prints
        // - display(0, 0) -> does not print
        void display(unsigned int& ignoreCount, unsigned int& displayCount) const;
};


#endif // __ANIMAL_H__