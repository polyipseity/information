#include "bst.h"
using namespace std;

/**
 * Returns true if "src" contains *any* words in "filterWords" (case-insensitive).
 * e.g.:
 *   containAnyWords("Example string", "example") == true
 *   containAnyWords("Example string", "amp") == true
 *   containAnyWords("Example string", "this is a long sentence") == true  [contains 'a']
 *   containAnyWords("Example string", "no occurence") == false
*/
bool containAnyWords(string src, string filterWords) {
    auto strToLower = [](string& str) {
        for (char& c: str) c = tolower(c);
    };
    strToLower(src);
    strToLower(filterWords);
    size_t found = filterWords.find(' ');
    while (found != string::npos) {
        if (src.find(filterWords.substr(0, found)) != string::npos)
            return true;
        filterWords = filterWords.substr(found+1);
        found = filterWords.find(' ');
    }
    return src.find(filterWords) != string::npos;
}


// TASK 2.1: Filter::match(const Animal&) const
// Returns true if the animal satisfies ALL 3 conditions:
// - species (including breed) contains *any* of the words in speciesMatch
// - health description contains *any* of the words in healthMatch
// - vaccine status contains *all* of the non-empty strings in vaccineMatch
bool Filter::match(const Animal& a) const
{

    // TODO
    if (!(containAnyWords(a.getSpecies(), speciesFilter) && containAnyWords(a.getHealthCondition().description, healthFilter)))
        return false;
    for (size_t idx{}; idx < sizeof(vaccineFilter) / sizeof(*vaccineFilter); ++idx)
    {
        if (!vaccineFilter[idx].empty() && !a.getVaccinationStatus().hasVaccine(vaccineFilter[idx]))
            return false;
    }

    return true;
}

// TASK 2.2: AnimalLLnode::print(unsigned int&, unsigned int&, const Filter&) const
// Print the animals in this linked list if it matches with the filter.
// The linked list should be maintained such that it is in decreasing ID order.
//
// E.g. (each node is shown as ID[Name]):
//      7[Cat] -> 6[Cat] -> 5[Dog] -> 3[Cat] -> 1[Bird] -> 0[Cat]
// should be printed in the following order using Filter{Name = "Cat"}:
//      0[Cat]
//      3[Cat]
//      6[Cat]
//      7[Cat]
//
// The parameters ignoreCount and displayCount should be passed to the animal's display() function
void AnimalLLnode::print(unsigned int& ignoreCount, unsigned int& displayCount, const Filter& filter) const
{

    // TODO
    if (next)
        next->print(ignoreCount, displayCount, filter);
    if (animal && filter.match(*animal))
        animal->display(ignoreCount, displayCount);
}

// TASK 2.3: BSTnode destructor
BSTnode::~BSTnode()  {

    // TODO
    for (AnimalLLnode *node{head}; node;)
    {
        AnimalLLnode *next{node->next};
        delete node;
        node = next;
    }
}

// TASK 2.4: BSTnode::addAnimal(const Animal* a)
// Add an animal to the linked list.
// Ensure the order is *decreasing ID*, e.g.: 7[Cat] -> 6[Cat] -> 5[Dog] -> 3[Cat] -> 1[Bird] -> 0[Cat]
// You may assume no two animals with the same ID will be added to a node
// (this also means you should not add the same animal to a node twice!)
void BSTnode::addAnimal(const Animal* a) {

    // TODO
    if (!head || (head->animal && head->animal->getID() < a->getID()))
    {
        head = new AnimalLLnode{a, head};
        return;
    }
    if (head->animal->getID() == a->getID())
        return;

    for (AnimalLLnode *node{head}; node; node = node->next)
    {
        if (!node->next || !node->next->animal)
        {
            node->next = new AnimalLLnode{a, node->next};
            return;
        }
        if (node->next->animal->getID() == a->getID())
            return;
        if (node->next->animal->getID() < a->getID())
        {
            node->next = new AnimalLLnode{a, node->next};
            break;
        }
    }
}

// TASK 2.5: BSTnode::addAnimal(const Animal* a)
// Remove an animal from the linked list.
// Ensure the order of the other animals are kept.
// If the animal does not exist, do nothing.
// If there are no animals left after removing, set head to nullptr.
void BSTnode::removeAnimal(const Animal* a) {

    // TODO
    for (AnimalLLnode *prev{}, *node{head}; node; prev = node, node = node->next)
    {
        if (node->animal && node->animal->getID() == a->getID())
        {
            if (prev)
                prev->next = node->next;
            else
                head = node->next;
            delete node;
            break;
        }
    }
}


// TASK 3.1: BST destructor
BST::~BST() {

    // TODO
    delete root;
}

// TASK 3.2: BST::findMinNode()
// Optional task, but may be needed for BST::remove().
// Return a reference to the BSTnode* of the min node in this BST.
BSTnode*& BST::findMinNode()
{

    // TODO
    if (!root)
        return root;
    BSTnode *&left_min{root->left.findMinNode()};
    if (left_min)
        return left_min;
    return root;
}

// TASK 3.3: BST::insert(const Animal* a)
// Insert an animal 'a' to the BST.
// Use the comparator "data member function" to compare the animal with the current node:
// - If 'a' is "less than" the current node, insert it to the left subtree.
// - If 'a' is "more than" the current node, insert it to the right subtree.
// - If 'a' "equals" the current node, insert it into this node's linked list.
// - Otherwise, if the node is empty, create a new node using 'a'.
void BST::insert(const Animal* a)
{

    // TODO
    if (!root)
        root = new BSTnode{a, comparator};
    else if (comparator(a, root->head->animal) < 0)
        root->left.insert(a);
    else if (comparator(a, root->head->animal) > 0)
        root->right.insert(a);
    else
        root->addAnimal(a);
}

// TASK 3.4: BST::remove(const Animal* a)
// Remove an animal 'a' from the BST
// Follow the same steps in BST::insert() to locate the node to remove.
// Removal strategy is similar to lecture notes example with a few differences:
// - If the node is not found, do nothing.
// - If the node is found, remove the animal from its linked list. If it makes the linked list become empty,
//   remove the node:
//   + If the node contains 0 or 1 child, move the children node to current root, and deallocate the old root.
//   + Else, *move* the linked list from the right subtree's min node to current root, and deallocate right subtree's min node.
void BST::remove(const Animal* a)
{

    // TODO
    if (!root)
        return;
    if (comparator(a, root->head->animal) < 0)
        root->left.remove(a);
    else if (comparator(a, root->head->animal) > 0)
        root->right.remove(a);
    else
    {
        root->removeAnimal(a);
        if (root->head)
            return;
        if (root->left.isEmpty())
        {
            BSTnode *old_root{root};
            root = old_root->right.root;
            old_root->right.root = nullptr;
            delete old_root;
            return;
        }
        if (root->right.isEmpty())
        {
            BSTnode *old_root{root};
            root = old_root->left.root;
            old_root->left.root = nullptr;
            delete old_root;
            return;
        }
        BSTnode *&right_min{root->right.findMinNode()};
        BSTnode *old_right_min{right_min};
        root->head = old_right_min->head;
        old_right_min->head = nullptr;
        right_min = old_right_min->right.root;
        old_right_min->right.root = nullptr;
        delete old_right_min;
    }
}

// TASK 3.5: BST::print(unsigned int&, unsigned int&, const Filter&) const
// Print the BST using in-order traversal.
//
// E.g.: Consider a BST containing animals sorted by species name:
//                      8[Reptile, Healthy] -> 6[Reptile, Bad]
//              5[Rabbit, Critical]
// 7[Dog, Healthy] -> 3[Dog, Healthy]
//                      9[Cat, Bad] -> 4[Cat, Healthy] -> 2[Cat, Very poor]
//              1[Bird, Healthy]
//
// should print in the following order using Filter{Health = "Healthy"}:
//      1[Bird, Healthy]
//      4[Cat, Healthy]
//      3[Dog, Healthy]
//      7[Dog, Healthy]
//      8[Reptile, Healthy]
void BST::print(unsigned int& ignoreCount, unsigned int& displayCount, const Filter& filter) const
{

    // TOD
    if (!root)
        return;
    root->left.print(ignoreCount, displayCount, filter);
    root->head->print(ignoreCount, displayCount, filter);
    root->right.print(ignoreCount, displayCount, filter);
}
