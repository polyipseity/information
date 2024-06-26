#ifndef PRODUCT_COLLECTION_H
#define PRODUCT_COLLECTION_H

#include <string>
using namespace std;

class ProductCollection {
private:
    string collectionID; // ID of the collection
    int* products; // dynamic array of product IDs
    int capacity; // capacity of the product array
    int size; // current number of products (integers) in the product array
public:
    ProductCollection(const string& collectionID, int capacity);
    ~ProductCollection();
    string getCollectionID() const; // returns collectionID
    int getCapacity() const; // returns the product array capacity
    int getSize() const; // returns current number of products in the array
    int readProduct(int i) const; // returns i-th product in the array
    void printProducts() const; // prints out all products
    int insert(int productID);
    bool contain(int productID) const;
    int remove(int productID);
    void increaseCapacity(int additionalSpace); // TODO 1
};
#endif