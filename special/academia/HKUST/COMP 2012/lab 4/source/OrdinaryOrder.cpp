#include <string>
#include <iostream>
#include "OrdinaryOrder.h"


using namespace std;

OrdinaryOrder::OrdinaryOrder(const string& collectionID, const string& name, OrderType type, int capacity)
    : ProductCollection{collectionID, capacity}, name{collectionID}, type{type}
{
    // TODO 2.1
    // You can use MIL for TODO 2.1 so you can modify the above part and your code does not neccessarily start from here

    // Your code ends here
    std::cout << "create " << getCollectionID() << ": OrdinaryOrder constructor" << std::endl;
}

int OrdinaryOrder::addFromOrder(const OrdinaryOrder* anotherOrder) {
    // TODO 2.2
    // Your code starts here

    if (getSize() + anotherOrder->getSize() > getCapacity())
        return 1;
    for (int idx{}; idx < anotherOrder->getSize(); ++idx)
        insert(anotherOrder->readProduct(idx));
    return 0;

    // Your code ends here
}