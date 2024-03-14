#include "OrderList.h"
#include <iostream>
#include <algorithm> // For copy
#include <new>       // For bad_alloc

// Task 5.1
OrderList::OrderList(){

}

// Task 5.2
OrderList::~OrderList() {

}

// Task 5.3
void OrderList::addOrder(const Order& order) {

}

// Task 5.4
bool OrderList::removeOrder(int orderId) {

}

// Task 5.5
Order* OrderList::findOrder(int orderId) const {

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
}

// Task 5.8
void OrderList::displayOrdersForBuyer(int buyerId) const {

// ------------Write your code here to complete this task-----------------


// ---------------------- provided code: DO NOT MODIFY --------------------------
    if (!found) {
        cout << "No orders found for Buyer ID: " << buyerId << endl;
    }
}


