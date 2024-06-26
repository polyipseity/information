#include "randomAnimalGenerator.h"
#include "animal.h"
#include <vector>
#include <map>
#include <string>
using namespace std;

/* -------------------------------------------------------------- */
/* This part serves as a pseudo random number generator for auto grade purpose only */
/* You are suggested not to refer to these codes in this assignment. */
/* You are not allowed to use global variables in this course. */
unsigned int next_num = 1; // Here we initiate an unsigned integer to be used in the following functions.

unsigned int pa3_rand() // This function is used to return a pseudo random number from 0 to 32767.
{
    next_num = next_num * 1103515245 + 2011;
    return static_cast<unsigned int>(next_num / 65536) % 32768;
}

void pa3_srand(unsigned int seed) // This function is used to set a seed of the pseudo random number generator.
{
    next_num = seed;
}

const vector<string> SPECIES = {"Cat", "Dog", "Rabbit", "Bird", "Reptiles"};

const map<string, vector<string>> BREEDS = {
    {"Cat", {
        "Ragdoll",
        "Maine Coon",
        "British Shorthair",
        "Scottish Fold",
        "Siamese",
        "Persian",
        "Bengal",
    }},
    {"Dog", {
        "French Bulldog",
        "Labrador Retriever",
        "Golden Retriever",
        "German Shepherd Dog",
        "Siberian Huskey",
        "Bulldog",
        "Rottweiler",
        "Beagle",
        "Daschund",
        "Poodle",
    }},
    {"Rabbit", {
        "Netherland Dwarf",
        "Dwarf Hotot",
        "Holland Lop",
        "English Lop",
        "Dutch",
        "Rex",
        "Californian",
        "Lionhead",
        "English Angora",
        "Flemish Giant",
    }},
    {"Bird", {
        "Budgerigar",
        "Cockatiel",
        "Cockatoo",
        "Hyacinth Macaw",
        "Dove",
        "Parrotlet",
        "Green-Cheeked Conure",
        "Hahn\'s Macaw",
        "Eclectus Parrot",
        "Canary Finch",
    }},
    {"Reptiles", {
        "Ball Python",
        "Leopard Gecko",
        "Guinea pig",
        "Hamster",
        "Russian Tortoise",
        "Corn Snakes",
        "King Snakes",
        "Crested Gecko",
    }},
};

const vector<HealthCondition> HEALTH_CONDITION = {
    HealthCondition{"Critical", 900},
    HealthCondition{"Very poor", 700},
    HealthCondition{"Poor", 500},
    HealthCondition{"Bad", 300},
    HealthCondition{"Fair", 100},
};

HealthCondition getRandomHealthCondition() {
    HealthCondition randHC = HEALTH_CONDITION[pa3_rand() % HEALTH_CONDITION.size()];
    randHC.severity += (static_cast<int>(pa3_rand() % 199 + 1) - 100);
    return randHC;
}

const map<string, vector<string>> VACCINES = {
    {"Cat", {
        "Rabies",
        "FPV",
        "FCV",
        "FHV",
        "FeLV",
        "FIV",
        "Chlamydia felis",
        "Bordetella bronchiseptica",
        "FIP",
        "Giardia",
    }},
    {"Dog", {
        "Rabies",
        "Canine Distemper",
        "Canine Parvovirus",
        "CAV-2",
        "Canine Parainfluenza",
        "Canine Bordetella",
        "Canine Leptospirosis",
        "Canine Coronavirus",
        "Lyme Disease",
        "Canine Influenza",
    }},
    {"Rabbit", {
        "RHDV",
        "Myxomatosis",
        "RCD",
        "Pasteurellosis",
        "Bordetella bronchiseptica",
        "E. cuniculi",
        "Filavac VHD K C+V",
        "Filavac Myxo-RHD PLUS",
        "Filavac RHD AS",
        "Filavac RHD R2",
    }},
    {"Bird", {
        "Avian Polyomavirus",
        "Avian Influenza",
        "PBFD",
        "Psittacosis",
        "Poxvirus",
        "Newcastle Disease",
        "Marek\'s Disease",
        "Gumboro",
        "West Nile Virus",
        "Candidiasis",
    }},
    {"Reptiles", {
        "Ranavirus",
        "Herpesvirus",
        "Salmonella",
        "Adenovirus",
        "Paramyxovirus",
        "Mycoplasma",
        "Eastern Box Turtle Herpesvirus",
        "Iridovirus",
        "Chelonid Herpesvirus",
        "SFD",
    }},
};

const vector<string> SPECIAL_NEEDS = {
    "Hand feeding",
    "Wound cleaning",
    "Antibacterial medicine",
    "Ear cleaning (infected)",
    "Eye cleaning (infected)",
};

unsigned int animalID = 0;

void shuffleVaccines(vector<string>& vaccines) {
    static unsigned int next_num = 1;
    for (unsigned int i=vaccines.size()-1; i>=1; --i) {
        next_num = next_num * 1103515245 + 2011;
        unsigned int j = (static_cast<unsigned int>(next_num / 65536) % 32768) % i;
        string temp = vaccines[i];
        vaccines[i] = vaccines[j];
        vaccines[j] = temp;
    }
}

Animal* createRandomAnimal() {
    string species = SPECIES[pa3_rand() % SPECIES.size()];
    return new Animal{
        animalID++,
        Species{
            species,
            pa3_rand() % 10 == 0 ? "N/A" : BREEDS.at(species)[pa3_rand() % BREEDS.at(species).size()],
        },
        pa3_rand() % 30,
        pa3_rand() % 6 > 0 ? NORMAL_HEALTH : getRandomHealthCondition(),
        pa3_rand() % 3 == 0 ? VaccinationStatus() : [species]() -> VaccinationStatus {
            unsigned int numVaccines = pa3_rand() % 5 + 1;
            VaccinationStatus v{};
            vector<string> availableVaccines = VACCINES.at(species);
            shuffleVaccines(availableVaccines);
            for (unsigned int i=0; i<numVaccines; ++i) {
                v.addVaccine(availableVaccines.back());
                availableVaccines.pop_back();
            }
            return v;
        }(),
        pa3_rand() % 10 > 0 ? "" : SPECIAL_NEEDS[pa3_rand() % SPECIAL_NEEDS.size()],
    };
}
/* -------------------------------------------------------------- */