#include <string>
#include <iostream>
#include "ProductCollection.h"

using namespace std;

ProductCollection::ProductCollection(const string& collectionID, int capacity) : collectionID(collectionID), capacity(capacity), size(0) {
    products = new int[capacity];
    std::cout << "create " << collectionID << ": ProductCollection constructor" <<  std::endl;
}

ProductCollection::~ProductCollection() {
    delete[] products;
}

string ProductCollection::getCollectionID() const {
    return collectionID;
}

int ProductCollection::getCapacity() const {
    return capacity;
}

int ProductCollection::getSize() const {
    return size;
}

int ProductCollection::readProduct(int i) const {
    return products[i];
}

void ProductCollection::printProducts() const {
    std::cout << collectionID << ": has product";
    for (int i = 0; i < size; i++) {
        std::cout << " " << products[i];
    }
    std::cout << std::endl;
}

int ProductCollection::insert(int productID) {
    if (size == capacity) {
        // capacity of array products[] is full, failed, cancel and return 1
        return 1;
    }
    products[size++] = productID;
    // successfully insert productID to the array products[], return 0
    return 0;
}

bool ProductCollection::contain(int productID) const {
    for (int i = 0; i < size; i++) {
        if (products[i] == productID) {
            // successfully found one productID in the array, return true
            return true;
        }
    }
    // no productID exist in the array, return false
    return false;
}

int ProductCollection::remove(int productID) {
    int i;
    
    for (i = 0; i < size; i++) {
        if (products[i] == productID) {
            break;
        }
    }
    
    // productID not found, cancel remove, return 1
    if (i == size) {
        return 1;
    }
    
    // Shift products forward
    for (int j = i; j < size - 1; j++) {
        products[j] = products[j + 1];
    }
    size--;
    
    // successfully remove the first-found productID, return 0
    return 0;
}

void ProductCollection::increaseCapacity(int additionalSpace) {
    // TODO 1
    // Your code starts here









    // Your code ends here
}
