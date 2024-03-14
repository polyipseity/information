#ifndef ORDER_LIST_H
#define ORDER_LIST_H

#include <iostream>
#include <string>
#include "Order.h"
#include "Buyer.h"
using namespace std;

class OrderList {
public:
    OrderList();
    ~OrderList();
    
    void addOrder(const Order& order);
    bool removeOrder(int orderId);
    Order* findOrder(int orderId) const;
    void displayOrderList() const;
    void displayOrdersForBuyer(int buyerId) const;
    bool isEmpty() const;

private:
    struct OrderNode {
        Order order;
        OrderNode* next;
        const Buyer& buyer = order.getBuyer();  // Get a reference to the Buyer object
        OrderNode(const Order& order, OrderNode* next = nullptr) : order(order), next(next) {}
    };

    OrderNode* head; // Pointer to the first node in the linked list
};


#endif // ORDER_LIST_H
