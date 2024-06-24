#ifndef __BST_H__
#define __BST_H__

#include <iostream>
#include "animal.h"

/**
 * Struct representing a filter.
 * The vaccineFilter is an array of length VACCINE_TABLE_SIZE.
 * Empty strings represents "any match".
*/
struct Filter {
    std::string speciesFilter {""};
    std::string healthFilter {""};
    std::string vaccineFilter[VACCINE_TABLE_SIZE] {};

    bool match(const Animal& a) const;
};

// Forward declaration
struct AnimalLLnode;
struct BSTnode;
typedef int (*AnimalComparator)(const Animal*, const Animal*);

/**
 * BST class for sorting Animal pointers.
 * 
 * This is structured similar to the lecture notes example,
 * except "T value" is replaced with "AnimalLLnode*", a linked list of Animal pointers.
 * Additionally, contains a "data member function" for comparing Animals.
*/
class BST {
    // A friend function for testing purpose
    friend void printTest(const BST&, unsigned int);

    private:
        // The root node
        BSTnode* root;
        // The comparison function, to be specified in the constructor
        const AnimalComparator comparator;

        // An optional private member function to retrieve the minimum-value node
        BSTnode*& findMinNode();
    
    public:
        // Constructor
        BST(const AnimalComparator comparator): root(nullptr), comparator(comparator) {}
        // Destructor
        ~BST();

        // Check if the BST is empty
        bool isEmpty() const { return root == nullptr; }

        // Insert and remove animals
        void insert(const Animal*);
        void remove(const Animal*);

        // Print the BST using in-order traversal
        void print(unsigned int& ignoreCount, unsigned int& displayCount, const Filter& filter) const;
};

/**
 * Struct representing a node in the Animal* linked list.
 * Contains a pointer to an Animal and a pointer to the next node,
 * which is nullptr if there is no next node.
 * 
 * The linked list should be maintained to have the animals in *decreasing ID* order.
*/
struct AnimalLLnode {
    const Animal* animal;
    AnimalLLnode* next;

    // Constructor
    AnimalLLnode(const Animal* a, AnimalLLnode* next = nullptr): animal(a), next(next) {}
    // Default destructor, performs no deallocation
    ~AnimalLLnode() = default;

    // Print the linked list of animals, with the current node as the head
    void print(unsigned int& ignoreCount, unsigned int& displayCount, const Filter& filter) const;
};

/**
 * Struct representing a node in the BST.
 * Contains a pointer to the Animal* linked list of this node, and 2 child BSTs.
*/
struct BSTnode {
    AnimalLLnode* head;
    BST left;
    BST right;
    
    // Constructor, initializes the linked list to have 1 node
    // Note that no BSTnode should contain no animals; it should be deleted as soon as there are none
    BSTnode(const Animal* a, const AnimalComparator c) : head(new AnimalLLnode(a, nullptr)), left(c), right(c) { }

    // Copy constructor and assignment operator are deleted
    BSTnode(const BSTnode&) = delete;
    BSTnode& operator=(const BSTnode&) = delete;

    // Destructor
    ~BSTnode();

    // Insert and remove animals
    void addAnimal(const Animal* a);
    void removeAnimal(const Animal* a);
};

#endif // __BST_H__