#ifndef MEMBER_ORDER_H
#define MEMBER_ORDER_H

#include <string>
#include "OrdinaryOrder.h"

using namespace std;

class MemberOrder : public OrdinaryOrder {
private:
    float rewardPoints; // reward points the products in this order can gain, 0.5 for each product
public:
    MemberOrder(const string& orderID, const string& name, OrderType type, int capacity); // TODO 3.1
    float getPoints() const;
    void insert(int productID); // TODO 3.2
    void remove(int productID); // TODO 3.2
    void addFromOrder(const OrdinaryOrder* anotherOrder); // TODO 3.3
};
#endif