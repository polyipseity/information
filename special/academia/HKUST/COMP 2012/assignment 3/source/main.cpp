#include <iostream>
using namespace std;

#include "animal.h"
#include "bst.h"
#include "adoptionCenter.h"
#include "randomAnimalGenerator.h"

string criteriaToString(SortCriteria c) {
    string str[] = {"Species Name", "Age", "Health Condition", "Vaccination Status", "ID"};
    return str[c];
}

ostream& operator<<(ostream& os, const Filter& f) {
    os << "Species = " << (f.speciesFilter.length() > 0 ? f.speciesFilter : "None") << "; "
        << "Health Condition = " << (f.healthFilter.length() > 0 ? f.healthFilter : "None") << "; "
        << "Vaccines: ";
    if (f.vaccineFilter[0].length() == 0)
        os << "None";
    else {
        os << f.vaccineFilter[0];
        for (unsigned int i=1; i<VACCINE_TABLE_SIZE; ++i)
            if (f.vaccineFilter[i].length() > 0)
                os << ", " << f.vaccineFilter[i];
    }
    return os;
}

int main() {
    AdoptionCenter adoptionCenter;
    for (int i=0; i<500; ++i) {
        adoptionCenter.addAnimal(createRandomAnimal());
    }

    for (int i=3; i<500; i += 5) {
        adoptionCenter.removeAnimal(i);
    }

    for (int i=500; i<700; ++i) {
        adoptionCenter.addAnimal(createRandomAnimal());
    }

    for (int i=507; i<700;  i+=11) {
        adoptionCenter.removeAnimal(i);
    }

    unsigned int displayCount = 20;
    Filter filter {};
    SortCriteria sortCriteria = ID;

    cout << "Welcome to the Pet Adoption Center Management System." << endl;
    while (true) {
        cout << "Select your choice:" << endl;
        cout << "1. View available pets" << endl;
        cout << "2. Set filter (current filter: " << filter << ")" << endl;
        cout << "3. Change sort criteria (current criteria: " << criteriaToString(sortCriteria) << ")" << endl; 
        cout << "4. Change display count (current display amount: " << displayCount << ")" << endl;
        cout << "5. View pet's taken vaccines" << endl;
        cout << "6. Admin options" << endl;
        cout << "7. Exit" << endl; 
        int choice;
        cin >> choice;

        switch (choice) {
            case 1:
                {
                    unsigned int curPage = 1;
                    while (true) {
                        string padTrimString(const string& str, unsigned int length);
                        cout << "ID" << "\t" 
                            << padTrimString("Species (Breed)", 30) << "\t"
                            << "Age" << "\t"
                            << padTrimString("Health Condition", 15) << "\t"
                            << "Vaccines Taken" << "\t"
                            << padTrimString("Special Needs", 25) << endl;
                        cout << "=====================================================================================================" << endl;
                        unsigned int start = (curPage-1) * displayCount;
                        unsigned int stop = curPage * displayCount;
                        adoptionCenter.display(start, stop, filter, sortCriteria);
                        cout << "=====================================================================================================" << endl;
                        cout << "Page " << curPage << endl;
                        cout << "Enter < or > to go to previous or next page (enter anything else to exit)" << endl;
                        char option;
                        cin >> option;
                        if (option == '<')
                            curPage = (curPage == 1) ? 1 : (curPage - 1);
                        else if (option == '>')
                            curPage = curPage + 1;
                        else
                            break;
                    }
                }
                break;
            case 2:
                {
                    while (true) {
                        cout << "Filter settings:" << endl;
                        cout << "1. Set species search terms (current filter: " << filter.speciesFilter << ")" << endl;
                        cout << "2. Set health condition search terms (current filter: " << filter.healthFilter << ")" << endl;
                        cout << "3. Add vaccine to filter" << endl;
                        cout << "4. Remove vaccine from filter" << endl;
                        cout << "5. Exit" << endl;
                        int filterChoice;
                        cin >> filterChoice;
                        cin.get();

                        switch (filterChoice) {
                            case 1:
                                cout << "Enter filter string: " << endl;
                                getline(cin, filter.speciesFilter);
                                break;
                            case 2:
                                cout << "Enter filter string: " << endl;
                                getline(cin, filter.healthFilter);
                                break;
                            case 3: case 4:
                                {
                                    cout << "Current vaccines in filter: " << endl;
                                    for (unsigned int i = 0; i < VACCINE_TABLE_SIZE; ++i)
                                        if (filter.vaccineFilter[i].length() > 0)
                                            cout << filter.vaccineFilter[i] << endl;
                                    cout << "Enter vaccine name: " << endl;
                                    string vaccine;
                                    getline(cin, vaccine);
                                    for (unsigned int i = 0; i < VACCINE_TABLE_SIZE; ++i) {
                                        if (filter.vaccineFilter[i] == vaccine) {
                                            if (filterChoice == 3)
                                                cout << "Warning: Vaccine already in filter" << endl;
                                            else {
                                                for (unsigned int j = i; j < VACCINE_TABLE_SIZE-1; ++j)
                                                    filter.vaccineFilter[j] = filter.vaccineFilter[j+1];
                                            }
                                            break;
                                        }
                                        else if (filter.vaccineFilter[i].length() == 0) {
                                            if (filterChoice == 3)
                                                filter.vaccineFilter[i] = vaccine;
                                            else
                                                cout << "Warning: Vaccine not found in filter" << endl;
                                            break;
                                        }
                                    }
                                }
                                break;
                            default:
                                cout << "Unrecognized option." << endl;
                            case 5:
                                break;
                        }
                        if (filterChoice == 5) break;
                    }
                }
                break;
            case 3:
                {
                    int criteria;
                    do {
                        cout << "Choose criteria to sort the pets:" << endl;
                        for (SortCriteria c = NAME; c <= ID; c = static_cast<SortCriteria>(c+1))
                            cout << static_cast<int>(c) << ": " << criteriaToString(c) << endl;
                        cin >> criteria;
                        if (criteria < NAME || criteria > ID)
                            cout << "Error: Invalid criteria, please try again." << endl;
                    } while (criteria < NAME || criteria > ID);

                    sortCriteria = static_cast<SortCriteria>(criteria);
                }
                break;
            case 4:
                do {
                    cout << "Enter number of pets to display:" << endl;
                    cin >> displayCount;
                    if (displayCount < 1)
                        cout << "Error: Cannot display less than 1 option, please try again." << endl;
                } while (displayCount < 1);
                break;
            case 5:
                {
                    cout << "Enter animal ID to query: " << endl;
                    int id;
                    cin >> id;
                    adoptionCenter.displayPetVaccines(id);
                }
                break;
            case 6:
                while (true) {
                    cout << "Admin panel:" << endl;
                    cout << "1. Add animal" << endl;
                    cout << "2. Remove animal" << endl;
                    cout << "3. Increment all animals' ages" << endl;
                    cout << "4. Change animal's health condition" << endl;
                    cout << "5. Add vaccine to animal" << endl;
                    cout << "6. Change animal's special needs" << endl;
                    cout << "7. Exit" << endl;
                    int adminChoice;
                    cin >> adminChoice;

                    switch (adminChoice) {
                        case 1:
                            {
                                string species;
                                string breed;
                                unsigned int age;
                                HealthCondition healthCondition;
                                string vaccine = "";
                                VaccinationStatus vaccineStatus;
                                string specialNeeds;

                                cout << "Enter animal species name: " << endl;
                                cin.get();
                                getline(cin, species);

                                cout << "Enter animal breed: " << endl;
                                getline(cin, breed);

                                cout << "Enter animal age: " << endl;
                                cin >> age;

                                cout << "Enter animal's health severity (an int value from 0 [normal] to 1000 [bad]): " << endl;
                                cin >> healthCondition.severity;
                                if (healthCondition.severity < 0) {
                                    cout << "Warning: Limiting severity value to 0" << endl;
                                    healthCondition.severity = 0;
                                }
                                if (healthCondition.severity > 1000) {
                                    cout << "Warning: Limiting severity value to 1000" << endl;
                                    healthCondition.severity = 1000;
                                }
                                if (healthCondition.severity > 0) {
                                    cout << "Enter animal's health condition description: " << endl;
                                    cin.get();
                                    getline(cin, healthCondition.description);
                                }
                                else {
                                    cin.get();
                                    healthCondition = NORMAL_HEALTH;
                                }

                                cout << "Enter animal's taken vaccines, one by one (press Enter to finish): " << endl;
                                do {
                                    getline(cin, vaccine);
                                    if (vaccine.length() > 0)
                                        vaccineStatus.addVaccine(vaccine);
                                } while (vaccine.length() > 0);

                                cout << "Enter animal's special needs, if any: " << endl;
                                getline(cin, specialNeeds);

                                adoptionCenter.addAnimal(new Animal(animalID, Species{species, breed}, age, healthCondition, vaccineStatus, specialNeeds));
                            }
                            break;
                        case 2:
                            {
                                cout << "Enter animal ID to remove: " << endl;
                                int id;
                                cin >> id;
                                if (!adoptionCenter.removeAnimal(id))
                                    cout << "Warning: ID not found in database" << endl;
                            }
                            break;
                        case 3:
                            adoptionCenter.incrementAge();
                            break;
                        case 4:
                            {
                                cout << "Enter animal ID to modify: " << endl;
                                int id;
                                cin >> id;

                                HealthCondition healthCondition;
                                cout << "Enter animal's health severity (an int value from 0 [normal] to 1000 [bad]): " << endl;
                                cin >> healthCondition.severity;
                                if (healthCondition.severity < 0) {
                                    cout << "Warning: Limiting severity value to 0" << endl;
                                    healthCondition.severity = 0;
                                }
                                if (healthCondition.severity > 1000) {
                                    cout << "Warning: Limiting severity value to 1000" << endl;
                                    healthCondition.severity = 1000;
                                }
                                if (healthCondition.severity > 0) {
                                    cout << "Enter animal's health condition description: " << endl;
                                    cin.get();
                                    getline(cin, healthCondition.description);
                                }
                                else {
                                    cin.get();
                                    healthCondition = NORMAL_HEALTH;
                                }
                                adoptionCenter.setAnimalHealthCondition(id, healthCondition);
                            }
                            break;
                        case 5:
                            {
                                cout << "Enter animal ID to modify: " << endl;
                                int id;
                                cin >> id;

                                string vaccine;
                                cout << "Enter vaccine name: " << endl;
                                cin.get();
                                getline(cin, vaccine);
                                if (vaccine.length() > 0) {
                                    adoptionCenter.addAnimalVaccine(id, vaccine);
                                }
                                else {
                                    cout << "Warning: Vaccine name cannot be empty." << endl;
                                }
                            }
                            break;
                        case 6:
                            {
                                cout << "Enter animal ID to modify: " << endl;
                                int id;
                                cin >> id;

                                string specialNeeds;
                                cout << "Enter new special needs description: " << endl;
                                cin.get();
                                getline(cin, specialNeeds);
                                adoptionCenter.setAnimalSpecialNeeds(id, specialNeeds);
                            }
                            break;
                        default:
                            cout << "Unrecognized option." << endl;
                        case 7:
                            break;
                    }
                    if (adminChoice == 7) break;
                }
                break;
            case 7:
                exit(0);
            default:
                cout << "Unrecognized option." << endl;
                break;
        }
    }
}