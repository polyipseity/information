#include "OrderList.h"
#include <iostream>
#include <algorithm> // For copy
#include <new>       // For bad_alloc

// Task 5.1
OrderList::OrderList() : head{} {

}

// Task 5.2
OrderList::~OrderList() {
    for (OrderNode *iter{head}; iter;)
    {
        OrderNode *next{iter->next};
        delete iter;
        iter = next;
    }
}

// Task 5.3
void OrderList::addOrder(const Order& order) {
    if (head)
    {
        OrderNode *tail{head};
        for (; tail->next; tail = tail->next)
            ;
        tail->next = new OrderNode{order};
        return;
    }
    head = new OrderNode{order};
}

// Task 5.4
bool OrderList::removeOrder(int orderId) {
    for (OrderNode *prev{}, *iter{head}; iter; prev = iter, iter = iter->next)
    {
        if (iter->order.getOrderId() == orderId)
        {
            if (prev)
                prev->next = iter->next;
            else
                head = iter->next;
            delete iter;
            return true;
        }
    }
    return false;
}

// Task 5.5
Order* OrderList::findOrder(int orderId) const {
    for (OrderNode *iter{head}; iter; iter = iter->next)
    {
        if (iter->order.getOrderId() == orderId)
            return &iter->order;
    }
    return nullptr;
}

// Task 5.6
bool OrderList::isEmpty() const {
  return head == nullptr;
}

// Task 5.7
void OrderList::displayOrderList() const {
// ---------------------- provided code: DO NOT MODIFY --------------------------
    cout << "Order List:" << endl;
    if (head == nullptr) {
        cout << "The order list is empty." << endl;
        return;
    }

// ------------Write your code here to complete this task-----------------
    for (OrderNode *iter{head}; iter; iter = iter->next)
        iter->order.displayOrder();
}

// Task 5.8
void OrderList::displayOrdersForBuyer(int buyerId) const {

// ------------Write your code here to complete this task-----------------
    bool found{};
    for (OrderNode *iter{head}; iter; iter = iter->next)
    {
        if (iter->buyer.getBuyerId() == buyerId)
        {
            found = true;
            iter->order.displayOrder();
        }
    }

// ---------------------- provided code: DO NOT MODIFY --------------------------
    if (!found) {
        cout << "No orders found for Buyer ID: " << buyerId << endl;
    }
}


