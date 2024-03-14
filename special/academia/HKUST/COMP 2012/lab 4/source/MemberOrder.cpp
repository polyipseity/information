#include <string>
#include <iostream>
#include "MemberOrder.h"

using namespace std;

MemberOrder::MemberOrder(const string& orderID, const string& name, OrderType type, int capacity) {
    // TODO 3.1
    // You can use MIL for TODO 3.1 so you can modify the above part and your code does not neccessarily start from here.

    // Your code ends here
    std::cout << "create " << getCollectionID() << ": MemberOrder constructor" << std::endl;
}

float MemberOrder::getPoints() const {
    return rewardPoints;
}

void MemberOrder::insert(int productID) {
    // TODO 3.2
    // Your code starts here





    // Your code ends here
}

void MemberOrder::remove(int productID) {
    // TODO 3.2
    // Your code starts here





    // Your code ends here
}

void MemberOrder::addFromOrder(const OrdinaryOrder* anotherOrder) {
    // TODO 3.3
    // Your code starts here






    // Your code ends here
}