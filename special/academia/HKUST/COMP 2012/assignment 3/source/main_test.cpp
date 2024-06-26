#include <iostream>
#include <vector>
using namespace std;

#include "animal.h"
#include "bst.h"
#include "adoptionCenter.h"
#include "randomAnimalGenerator.h"

void printVaccineTable(const VaccinationStatus& v) {
    unsigned int sumStringChars(const string& str);
    for (unsigned int i=0; i<VACCINE_TABLE_SIZE; ++i) {
        cout << "[" << i << "]: " << v.vaccineHashTable[i];
        if (v.vaccineHashTable[i].length() > 0)
            cout << " (" << sumStringChars(v.vaccineHashTable[i]) % VACCINE_TABLE_SIZE << ")";
        cout << endl;
    }
}

void test1() {
    VaccinationStatus v{};
    cout << "Empty Vaccine hash table count: " << v.numVaccines << endl;
}

/***********************************************************************/

void addVaccines(VaccinationStatus& v, const vector<string>& vaccines) {
    for (string vac : vaccines)
        v.addVaccine(vac);
}

void test2() {
    VaccinationStatus v{};
    addVaccines(v, {"Rabies"});
    printVaccineTable(v);
}

void test3() {
    VaccinationStatus v{};
    addVaccines(v, {"Rabies", "FPV", "FCV"});
    printVaccineTable(v);
}

void test4() {
    VaccinationStatus v{};
    addVaccines(v, {"Rabies", "FPV", "FCV", "FHV", "FeLV"});
    printVaccineTable(v);
}

void test5() {
    VaccinationStatus v{};
    addVaccines(v, {"Rabies", "FPV", "FCV", "FHV", "FeLV", "FIV", "Chlamydia felis"});
    printVaccineTable(v);
}

void test6() {
    VaccinationStatus v{};
    addVaccines(v, {"Rabies", "FPV", "FCV", "FHV", "FeLV", "FIV", "Chlamydia felis", "Bordetella bronchiseptica", "Giardia"});
    printVaccineTable(v);
}

/***********************************************************************/

void test7() {
    VaccinationStatus v{};
    addVaccines(v, {"Rabies", "FPV", "FCV", "FHV", "FeLV", "FIV", "Chlamydia felis", "Bordetella bronchiseptica", "Giardia"});
    cout << "Contains vaccine FPV: " << v.hasVaccine("FPV") << endl; 
}

void test8() {
    VaccinationStatus v{};
    addVaccines(v, {"Rabies", "FPV", "FCV", "FHV", "FeLV", "FIV", "Chlamydia felis", "Bordetella bronchiseptica", "Giardia"});
    cout << "Contains vaccine Giardia: " << v.hasVaccine("Giardia") << endl; 
}

/***********************************************************************/

Filter makeFilter(const string& s, const string& h, const vector<string>& v) {
    Filter f;
    f.speciesFilter = s;
    f.healthFilter = h;
    for (unsigned int i=0; i<v.size(); ++i)
        f.vaccineFilter[i] = v[i];
    return f;
}

Animal testAnimal = {
    0,
    Species{"Cat", "British Shorthair"},
    20,
    HealthCondition{"Very poor", 800},
    []() -> VaccinationStatus {
        VaccinationStatus v{};
        addVaccines(v, {"FPV", "FCV", "FHV"});
        return v;
    }(),
};

void test9() {
    Filter f = makeFilter(
        "cat short",
        "Poor",
        {"FCV", "FPV"}
    );
    cout << "Animal match: " << f.match(testAnimal) << endl;
}

void test10() {
    Filter f = makeFilter(
        "dog",
        "",
        {}
    );
    cout << "Animal match: " << f.match(testAnimal) << endl;
}

void test11() {
    Filter f = makeFilter(
        "cat",
        "Poor",
        {"FPV", "Rabies"}
    );
    cout << "Animal match: " << f.match(testAnimal) << endl;
}

/***********************************************************************/

void test12() {
    const int NUM_NODES = 4;
    AnimalLLnode* nodes[NUM_NODES];
    for (int i=0; i<NUM_NODES; ++i)
        nodes[i] = new AnimalLLnode(createRandomAnimal(), i == 0 ? nullptr : nodes[i-1]);
    
    unsigned int ignoreCount = 0;
    unsigned int displayCount = 4;
    nodes[NUM_NODES-1]->print(ignoreCount, displayCount, makeFilter("", "", {}));
    
    for (int i=0; i<NUM_NODES; ++i) {
        delete nodes[i]->animal;
        delete nodes[i];
    }
}

void test13() {
    const int NUM_NODES = 10;
    AnimalLLnode* nodes[NUM_NODES];
    for (int i=0; i<NUM_NODES; ++i)
        nodes[i] = new AnimalLLnode(createRandomAnimal(), i == 0 ? nullptr : nodes[i-1]);
    
    unsigned int ignoreCount = 2;
    unsigned int displayCount = 5;
    nodes[NUM_NODES-1]->print(ignoreCount, displayCount, makeFilter("", "", {}));
    
    for (int i=0; i<NUM_NODES; ++i) {
        delete nodes[i]->animal;
        delete nodes[i];
    }
}

void test14() {
    const int NUM_NODES = 10;
    AnimalLLnode* nodes[NUM_NODES];
    for (int i=0; i<NUM_NODES; ++i)
        nodes[i] = new AnimalLLnode(createRandomAnimal(), i == 0 ? nullptr : nodes[i-1]);
    
    unsigned int ignoreCount = 0;
    unsigned int displayCount = 10;
    nodes[NUM_NODES-1]->print(ignoreCount, displayCount, makeFilter("a", "", {}));
    
    for (int i=0; i<NUM_NODES; ++i) {
        delete nodes[i]->animal;
        delete nodes[i];
    }
}

/***********************************************************************/

int dummyAnimalComparator(const Animal* a, const Animal* b) {
    return (static_cast<int>(a->getID()) % 100) - (static_cast<int>(b->getID()) % 100);
}

void test15() {
    Animal* animal = createRandomAnimal();
    BSTnode bstNode {animal, dummyAnimalComparator};

    AnimalLLnode* head = bstNode.head;
    unsigned int ignoreCount = 0;
    unsigned int displayCount = 1;
    cout << "Displaying linked list nodes manually: " << endl;
    do {
        head->animal->display(ignoreCount, displayCount);
        head = head->next;
    } while (head);

    delete animal;
}

/***********************************************************************/

void test16() {
    const int NUM_ANIMALS = 5;
    Animal* animals[NUM_ANIMALS] {nullptr};
    for (int i=0; i<NUM_ANIMALS; ++i)
        animals[i] = createRandomAnimal();
    BSTnode bstNode {animals[0], dummyAnimalComparator};
    for (int i=1; i<NUM_ANIMALS; ++i)
        bstNode.addAnimal(animals[i]);
    
    AnimalLLnode* head = bstNode.head;
    unsigned int ignoreCount = 0;
    unsigned int displayCount = NUM_ANIMALS;
    cout << "Displaying linked list nodes manually: " << endl;
    do {
        head->animal->display(ignoreCount, displayCount);
        head = head->next;
    } while (head);

    for (int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
}

void test17() {
    const int NUM_ANIMALS = 10;
    Animal* animals[NUM_ANIMALS] {nullptr};
    int index[NUM_ANIMALS] = {4, 3, 8, 9, 5, 1, 2, 7, 6, 0};
    for (int i=0; i<NUM_ANIMALS; ++i)
        animals[index[i]] = createRandomAnimal();
    BSTnode bstNode {animals[0], dummyAnimalComparator};
    for (int i=1; i<NUM_ANIMALS; ++i) {
        cout << "Adding animal with ID " << animals[i]->getID() << endl;
        bstNode.addAnimal(animals[i]);
    }
    
    AnimalLLnode* head = bstNode.head;
    unsigned int ignoreCount = 0;
    unsigned int displayCount = NUM_ANIMALS;
    cout << "Displaying linked list nodes manually: " << endl;
    do {
        head->animal->display(ignoreCount, displayCount);
        head = head->next;
    } while (head);

    for (int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
}

/***********************************************************************/

void test18() {
    const int NUM_ANIMALS = 10;
    Animal* animals[NUM_ANIMALS] {nullptr};
    for (int i=0; i<NUM_ANIMALS; ++i)
        animals[i] = createRandomAnimal();
    BSTnode bstNode {animals[0], dummyAnimalComparator};
    for (int i=1; i<NUM_ANIMALS; ++i)
        bstNode.addAnimal(animals[i]);

    bstNode.removeAnimal(animals[5]);

    AnimalLLnode* head = bstNode.head;
    unsigned int ignoreCount = 0;
    unsigned int displayCount = 9;
    cout << "Displaying linked list nodes manually: " << endl;
    do {
        head->animal->display(ignoreCount, displayCount);
        head = head->next;
    } while (head);

    for (int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
}

void test19() {
    const int NUM_ANIMALS = 10;
    Animal* animals[NUM_ANIMALS] {nullptr};
    for (int i=0; i<NUM_ANIMALS; ++i)
        animals[i] = createRandomAnimal();
    BSTnode bstNode {animals[0], dummyAnimalComparator};
    for (int i=1; i<NUM_ANIMALS; ++i)
        bstNode.addAnimal(animals[i]);

    bstNode.removeAnimal(animals[7]);
    bstNode.removeAnimal(animals[2]);
    bstNode.addAnimal(animals[7]);

    AnimalLLnode* head = bstNode.head;
    unsigned int ignoreCount = 0;
    unsigned int displayCount = 9;
    cout << "Displaying linked list nodes manually: " << endl;
    do {
        head->animal->display(ignoreCount, displayCount);
        head = head->next;
    } while (head);

    for (int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
}

void test20() {
    const int NUM_ANIMALS = 3;
    Animal* animals[NUM_ANIMALS] {nullptr};
    for (int i=0; i<NUM_ANIMALS; ++i)
        animals[i] = createRandomAnimal();
    BSTnode bstNode {animals[0], dummyAnimalComparator};
    for (int i=1; i<NUM_ANIMALS; ++i)
        bstNode.addAnimal(animals[i]);
    for (int i=0; i<NUM_ANIMALS; ++i)
        bstNode.removeAnimal(animals[i]);

    cout << "Empty BSTnode's head is nullptr: " << (bstNode.head == nullptr) << endl;

    for (int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
}

/***********************************************************************/

/**
 * Note: The BST test cases (21 - 32) sort the animals by ID from 0 to 99.
 * Higher IDs are inserted into the same node as their modulo 100 (e.g. 105 and 5 are in the same node).
 * The BST is printed in a similar format as the lecture notes,
 * with the animals in the same node printed in a horizontal linked list.
*/

void printNode(const AnimalLLnode* const node) {
    cout << node->animal->getID();
    if (node->next) {
        cout << " -> ";
        printNode(node->next);
    }
    else
        cout << endl;
}

void printTest(const BST& bst, unsigned int depth = 0) {
    if (bst.isEmpty())
        return;
    printTest(bst.root->right, depth+1);
    for (unsigned int j = 0; j < depth; j++)
        cout << '\t';
    printNode(bst.root->head);
    printTest(bst.root->left, depth+1);
}

Animal* createRandomAnimalWithID(unsigned int id) {
    extern unsigned int animalID;
    animalID = id;
    return createRandomAnimal();
}

void test21() {
    BST bst{dummyAnimalComparator};
    const int NUM_ANIMALS = 10;
    Animal* animals[NUM_ANIMALS] {nullptr};
    int index[NUM_ANIMALS] = {4, 3, 8, 9, 5, 1, 2, 7, 6, 0};
    for (unsigned int i=0; i<NUM_ANIMALS; ++i) {
        animals[i] = createRandomAnimalWithID(index[i]);
        bst.insert(animals[i]);
    }
    printTest(bst);
    for (unsigned int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
}

void test22() {
    BST bst{dummyAnimalComparator};
    const int NUM_ANIMALS = 10;
    Animal* animals[NUM_ANIMALS] {nullptr};
    int index[NUM_ANIMALS] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    for (unsigned int i=0; i<NUM_ANIMALS; ++i) {
        animals[i] = createRandomAnimalWithID(index[i]);
        bst.insert(animals[i]);
    }
    printTest(bst);
    for (unsigned int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
}

void test23() {
    BST bst{dummyAnimalComparator};
    const int NUM_ANIMALS = 10;
    Animal* animals[NUM_ANIMALS * 2];
    int index[NUM_ANIMALS] = {4, 3, 8, 9, 5, 1, 2, 7, 6, 0};
    for (unsigned int i=0; i<NUM_ANIMALS; ++i) {
        animals[i] = createRandomAnimalWithID(index[i]);
        bst.insert(animals[i]);
    }
    for (unsigned int i=10; i<15; ++i) {
        animals[i] = createRandomAnimalWithID(i + 91);
        bst.insert(animals[i]);
    }
    for (unsigned int i=15; i<20; ++i) {
        animals[i] = createRandomAnimalWithID(i * 2 + 171);
        bst.insert(animals[i]);
    }
    printTest(bst);
    for (unsigned int i=0; i<NUM_ANIMALS*2; ++i)
        delete animals[i];
}

/***********************************************************************/

void test24() {
    BST bst{dummyAnimalComparator};
    const int NUM_ANIMALS = 15;
    Animal* animals[NUM_ANIMALS] {nullptr};
    int index[NUM_ANIMALS] = {4, 3, 8, 9, 11, 5, 1, 2, 7, 10, 14, 13, 12, 6, 0};
    for (unsigned int i=0; i<NUM_ANIMALS; ++i) {
        animals[i] = createRandomAnimalWithID(index[i]);
        bst.insert(animals[i]);
    }
    cout << "Removing id " << animals[13]->getID() << endl;
    bst.remove(animals[13]);
    printTest(bst);
    for (unsigned int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
}

void test25() {
    BST bst{dummyAnimalComparator};
    const int NUM_ANIMALS = 15;
    Animal* animals[NUM_ANIMALS] {nullptr};
    int index[NUM_ANIMALS] = {4, 3, 8, 9, 11, 5, 1, 2, 7, 10, 14, 13, 12, 6, 0};
    for (unsigned int i=0; i<NUM_ANIMALS; ++i) {
        animals[i] = createRandomAnimalWithID(index[i]);
        bst.insert(animals[i]);
    }
    cout << "Removing id " << animals[11]->getID() << endl;
    bst.remove(animals[11]);
    printTest(bst);
    for (unsigned int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
}

void test26() {
    BST bst{dummyAnimalComparator};
    const int NUM_ANIMALS = 15;
    Animal* animals[NUM_ANIMALS] {nullptr};
    int index[NUM_ANIMALS] = {4, 3, 8, 9, 11, 5, 1, 2, 7, 10, 14, 13, 12, 6, 0};
    for (unsigned int i=0; i<NUM_ANIMALS; ++i) {
        animals[i] = createRandomAnimalWithID(index[i]);
        bst.insert(animals[i]);
    }
    cout << "Removing id " << animals[6]->getID() << endl;
    bst.remove(animals[6]);
    printTest(bst);
    for (unsigned int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
}

void test27() {
    BST bst{dummyAnimalComparator};
    const int NUM_ANIMALS = 15;
    Animal* animals[NUM_ANIMALS] {nullptr};
    int index[NUM_ANIMALS] = {4, 3, 8, 9, 11, 5, 1, 2, 7, 10, 14, 13, 12, 6, 0};
    for (unsigned int i=0; i<NUM_ANIMALS; ++i) {
        animals[i] = createRandomAnimalWithID(index[i]);
        bst.insert(animals[i]);
    }
    cout << "Removing id " << animals[4]->getID() << endl;
    bst.remove(animals[4]);
    printTest(bst);
    for (unsigned int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
}

void test28() {
    BST bst{dummyAnimalComparator};
    const int NUM_ANIMALS = 15;
    Animal* animals[NUM_ANIMALS] {nullptr};
    int index[NUM_ANIMALS] = {4, 3, 8, 9, 11, 5, 1, 2, 7, 10, 14, 13, 12, 6, 0};
    for (unsigned int i=0; i<NUM_ANIMALS; ++i) {
        animals[i] = createRandomAnimalWithID(index[i]);
        bst.insert(animals[i]);
    }
    const int NUM_EXTRA_ANIMALS = 5;
    Animal* extraAnimals[NUM_EXTRA_ANIMALS];
    for (unsigned int i=0; i<NUM_EXTRA_ANIMALS; ++i) {
        extraAnimals[i] = createRandomAnimalWithID(i * 3 + 101);
        bst.insert(extraAnimals[i]);
    }
    cout << "Removing id " << animals[11]->getID() << endl;
    bst.remove(animals[11]);
    printTest(bst);
    for (unsigned int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
    for (unsigned int i=0; i<NUM_EXTRA_ANIMALS; ++i)
        delete extraAnimals[i];
}

void test29() {
    BST bst{dummyAnimalComparator};
    const int NUM_ANIMALS = 15;
    Animal* animals[NUM_ANIMALS] {nullptr};
    int index[NUM_ANIMALS] = {4, 3, 8, 9, 11, 5, 1, 2, 7, 10, 14, 13, 12, 6, 0};
    for (unsigned int i=0; i<NUM_ANIMALS; ++i) {
        animals[i] = createRandomAnimalWithID(index[i]);
        bst.insert(animals[i]);
    }
    const int NUM_EXTRA_ANIMALS = 5;
    Animal* extraAnimals[NUM_EXTRA_ANIMALS];
    for (unsigned int i=0; i<NUM_EXTRA_ANIMALS; ++i) {
        extraAnimals[i] = createRandomAnimalWithID(i * 3 + 102);
        bst.insert(extraAnimals[i]);
    }
    cout << "Removing id " << animals[6]->getID() << endl;
    bst.remove(animals[6]);
    printTest(bst);
    for (unsigned int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
    for (unsigned int i=0; i<NUM_EXTRA_ANIMALS; ++i)
        delete extraAnimals[i];
}

void test30() {
    BST bst{dummyAnimalComparator};
    const int NUM_ANIMALS = 15;
    Animal* animals[NUM_ANIMALS] {nullptr};
    int index[NUM_ANIMALS] = {4, 3, 8, 9, 11, 5, 1, 2, 7, 10, 14, 13, 12, 6, 0};
    for (unsigned int i=0; i<NUM_ANIMALS; ++i) {
        animals[i] = createRandomAnimalWithID(index[i]);
        bst.insert(animals[i]);
    }
    const int NUM_EXTRA_ANIMALS = 5;
    Animal* extraAnimals[NUM_EXTRA_ANIMALS];
    for (unsigned int i=0; i<NUM_EXTRA_ANIMALS; ++i) {
        extraAnimals[i] = createRandomAnimalWithID(i * 3 + 100);
        bst.insert(extraAnimals[i]);
    }
    cout << "Removing id " << animals[4]->getID() << endl;
    bst.remove(animals[4]);
    printTest(bst);
    for (unsigned int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
    for (unsigned int i=0; i<NUM_EXTRA_ANIMALS; ++i)
        delete extraAnimals[i];
}

/***********************************************************************/

void test31() {
    BST bst{dummyAnimalComparator};
    const int NUM_ANIMALS = 15;
    Animal* animals[NUM_ANIMALS] {nullptr};
    int index[NUM_ANIMALS] = {4, 3, 8, 9, 11, 5, 1, 2, 7, 10, 14, 13, 12, 6, 0};
    for (unsigned int i=0; i<NUM_ANIMALS; ++i) {
        animals[i] = createRandomAnimalWithID(index[i]);
        bst.insert(animals[i]);
    }
    const int NUM_EXTRA_ANIMALS = 5;
    Animal* extraAnimals[NUM_EXTRA_ANIMALS];
    for (unsigned int i=0; i<NUM_EXTRA_ANIMALS; ++i) {
        extraAnimals[i] = createRandomAnimalWithID(i * 3 + 100);
        bst.insert(extraAnimals[i]);
    }
    unsigned int ignoreCount = 0;
    unsigned int displayCount = 20;
    bst.print(ignoreCount, displayCount, makeFilter("", "", {}));
    for (unsigned int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
    for (unsigned int i=0; i<NUM_EXTRA_ANIMALS; ++i)
        delete extraAnimals[i];
}

void test32() {
    BST bst{dummyAnimalComparator};
    const int NUM_ANIMALS = 15;
    Animal* animals[NUM_ANIMALS] {nullptr};
    int index[NUM_ANIMALS] = {4, 3, 8, 9, 11, 5, 1, 2, 7, 10, 14, 13, 12, 6, 0};
    for (unsigned int i=0; i<NUM_ANIMALS; ++i) {
        animals[i] = createRandomAnimalWithID(index[i]);
        bst.insert(animals[i]);
    }
    const int NUM_EXTRA_ANIMALS = 5;
    Animal* extraAnimals[NUM_EXTRA_ANIMALS];
    for (unsigned int i=0; i<NUM_EXTRA_ANIMALS; ++i) {
        extraAnimals[i] = createRandomAnimalWithID(i * 3 + 100);
        bst.insert(extraAnimals[i]);
    }
    unsigned int ignoreCount = 3;
    unsigned int displayCount = 15;
    bst.print(ignoreCount, displayCount, makeFilter("", "Healthy", {}));
    for (unsigned int i=0; i<NUM_ANIMALS; ++i)
        delete animals[i];
    for (unsigned int i=0; i<NUM_EXTRA_ANIMALS; ++i)
        delete extraAnimals[i];
}

/***********************************************************************/

void test33() {
    AdoptionCenter center;
    for (unsigned int i=0; i<20; ++i) {
        center.addAnimal(createRandomAnimal());
    }
    center.display(0, 20, makeFilter("", "", {}));
}

void test34() {
    AdoptionCenter center;
    for (unsigned int i=0; i<20; ++i) {
        center.addAnimal(createRandomAnimal());
    }
    center.display(0, 20, makeFilter("", "", {}), NAME);
}

void test35() {
    AdoptionCenter center;
    for (unsigned int i=0; i<20; ++i) {
        center.addAnimal(createRandomAnimal());
    }
    center.display(0, 20, makeFilter("", "", {}), AGE);
}

void test36() {
    AdoptionCenter center;
    for (unsigned int i=0; i<20; ++i) {
        center.addAnimal(createRandomAnimal());
    }
    center.display(0, 20, makeFilter("", "", {}), HEALTH);
}

void test37() {
    AdoptionCenter center;
    for (unsigned int i=0; i<20; ++i) {
        center.addAnimal(createRandomAnimal());
    }
    center.display(0, 20, makeFilter("", "", {}), VACCINE);
}

/***********************************************************************/

void test38() {
    AdoptionCenter center;
    for (unsigned int i=0; i<50; ++i) {
        center.addAnimal(createRandomAnimal());
    }
    for (unsigned int i=3; i<50; i=i+7) {
        cout << "Remove ID " << i << " is successful: " << center.removeAnimal(i) << endl;
    }
}

/***********************************************************************/

void test39() {
    AdoptionCenter center;
    for (unsigned int i=0; i<20; ++i) {
        center.addAnimal(createRandomAnimal());
    }
    center.incrementAge();
    center.display(0, 20, makeFilter("", "", {}));
}

void test40() {
    AdoptionCenter center;
    for (unsigned int i=0; i<20; ++i) {
        center.addAnimal(createRandomAnimal());
    }
    center.setAnimalHealthCondition(5, HealthCondition{"Weak", 750});
    center.display(0, 20, makeFilter("", "", {}), HEALTH);
}

void test41() {
    AdoptionCenter center;
    for (unsigned int i=0; i<20; ++i) {
        center.addAnimal(createRandomAnimal());
    }
    center.addAnimalVaccine(6, "Paramyxovirus");
    center.display(0, 20, makeFilter("", "", {}), VACCINE);
}

void test42() {
    AdoptionCenter center;
    for (unsigned int i=0; i<20; ++i) {
        center.addAnimal(createRandomAnimal());
    }
    center.setAnimalSpecialNeeds(13, "Antibacterial medicine");
    center.display(0, 20, makeFilter("", "", {}));
}

/***********************************************************************/

void centerSetup(AdoptionCenter& center) {
    for (int i=0; i<500; ++i) {
        center.addAnimal(createRandomAnimal());
    }
    for (int i=3; i<500; i += 5) {
        center.removeAnimal(i);
    }
    for (int i=500; i<700; ++i) {
        center.addAnimal(createRandomAnimal());
    }
    for (int i=507; i<700;  i+=11) {
        center.removeAnimal(i);
    }
}

void test43() {
    AdoptionCenter center;
    centerSetup(center);
    center.display(0, 20, makeFilter("cat N/A", "Healthy", {"Rabies"}));
}

void test44() {
    AdoptionCenter center;
    centerSetup(center);
    center.display(0, 20, makeFilter("", "", {"Filavac RHD AS", "Pasteurellosis", "Bordetella bronchiseptica"}));
}

void test45() {
    AdoptionCenter center;
    centerSetup(center);
    center.incrementAge();
    center.display(30, 50, makeFilter("", "", {}), AGE);
}

void test46() {
    AdoptionCenter center;
    centerSetup(center);
    center.setAnimalHealthCondition(251, HealthCondition{"Very bad", 600});
    center.setAnimalSpecialNeeds(251, "Requires intensive care");
    center.display(0, 30, makeFilter("", "", {}), NAME);
}

void test47() {
    AdoptionCenter center;
    centerSetup(center);
    center.addAnimalVaccine(24, "Avian Polyomavirus");
    center.addAnimalVaccine(24, "Marek\'s Disease");
    center.addAnimalVaccine(24, "Candidiasis");
    center.addAnimalVaccine(274, "Poxvirus");
    center.display(0, 30, makeFilter("parrot", "", {}), VACCINE);
}

void test48() {
    AdoptionCenter center;
    centerSetup(center);
    center.removeAnimal(9);
    center.setAnimalHealthCondition(14, HealthCondition{"Healthy", 0});
    center.addAnimalVaccine(14, "Iridovirus");
    center.display(0, 30, makeFilter("", "", {}));
}

void test49() {
    AdoptionCenter center;
    centerSetup(center);
    for (int i=16; i<700; i+=23) {
        extern unsigned int pa3_rand();
        switch (pa3_rand() % 4) {
            case 0:
                center.removeAnimal(i);
                break;
            case 1:
                center.setAnimalHealthCondition(i, HealthCondition{"Custom text", 500});
                break;
            case 2:
                center.addAnimalVaccine(i, "Custom vaccine");
                break;
            case 3:
                center.setAnimalSpecialNeeds(i, "Custom text");
                break;
        }
    }
    center.display(500, 550, makeFilter("", "", {}), HEALTH);
}

void test50() {
    AdoptionCenter center;
    centerSetup(center);
    for (int i=4; i<700; i+=5) {
        extern unsigned int pa3_rand();
        switch (pa3_rand() % 4) {
            case 0:
                center.removeAnimal(i);
                break;
            case 1:
                center.setAnimalHealthCondition(i, HealthCondition{"Custom text", 500});
                break;
            case 2:
                center.addAnimalVaccine(i, "Custom vaccine");
                break;
            case 3:
                center.setAnimalSpecialNeeds(i, "Custom text");
                break;
        }
    }
    center.display(200, 250, makeFilter("", "", {}), VACCINE);
}

/***********************************************************************/

int main() {
    int test;
    cin >> test;
    cout << boolalpha;
    switch (test) {
        #define TEST(X) case X: test ## X(); break

        TEST(1); TEST(2); TEST(3); TEST(4); TEST(5); TEST(6); TEST(7); TEST(8);

        TEST(9); TEST(10); TEST(11); TEST(12); TEST(13); TEST(14);

        TEST(15); TEST(16); TEST(17); TEST(18); TEST(19); TEST(20);

        TEST(21); TEST(22); TEST(23); TEST(24); TEST(25); TEST(26); TEST(27); TEST(28); TEST(29); TEST(30);

        TEST(31); TEST(32);

        TEST(33); TEST(34); TEST(35); TEST(36); TEST(37); TEST(38);

        TEST(39); TEST(40); TEST(41); TEST(42);

        TEST(43); TEST(44); TEST(45); TEST(46); TEST(47); TEST(48); TEST(49); TEST(50);

        default:
            cout << "Unrecognized test case" << endl;
    }
}