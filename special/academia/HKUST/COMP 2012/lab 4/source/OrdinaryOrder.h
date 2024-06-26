#ifndef ORDINARY_ORDER_H
#define ORDINARY_ORDER_H

#include <string>
#include "ProductCollection.h"

using namespace std;

enum OrderType {ON_SITE, PICK_UP, COURIER}; // enumeration of delivery type

class OrdinaryOrder : public ProductCollection {
private:
    string name; // customer name of this order
    OrderType type; // delivery type of this order
public:
    OrdinaryOrder(const string& orderID, const string& name, OrderType type, int capacity); // TODO 2.1
    int addFromOrder(const OrdinaryOrder* anotherOrder); // TODO 2.2
};
#endif