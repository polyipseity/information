#ifndef __DATATYPES_H__
#define __DATATYPES_H__

#include <string>

/**
 * A struct representing the species and breed.
 * E.g.: Species{"Dog", "Poodle"} represents "Dog (Poodle)"
*/
struct Species {
    std::string name;
    std::string breed;
};

/**
 * A struct representing an animal's health condition.
 * E.g.: HealthCondition{"Very bad", 750} represents an animal with very bad health condition
*/
struct HealthCondition {
    std::string description;
    unsigned int severity;
};

// A constant represent "normal health condition"
const HealthCondition NORMAL_HEALTH {"Healthy", 0};

// Size of the vaccine hash table
const unsigned int VACCINE_TABLE_SIZE = 23;

/**
 * A struct representing the vaccination history.
 * Implemented as a hash table of strings, using quadratic probing open addressing strategy.
*/
struct VaccinationStatus {
    // The hash table
    std::string vaccineHashTable[VACCINE_TABLE_SIZE];
    // Number of vaccines currently in the table
    unsigned int numVaccines;

    // Default constructor
    VaccinationStatus();

    void addVaccine(const std::string& v);
    bool hasVaccine(const std::string& v) const;

    // Return a value representing the current hash table for comparison
    unsigned int getTotalHashValue() const;
};

#endif //__DATATYPES_H__