#ifndef ORDER_H
#define ORDER_H

#include "Food.h"
#include "Buyer.h"
#include <iostream>
#include <string>
using namespace std;

class Order {
private:
  int orderId;
  int currentNum;
  Food orderedItems[10];  // Array to hold ordered food items (fixed size)
  Buyer buyer;

public:
  Order();  // Default Constructor
  bool addItem(const Food& item);
  void displayOrder() const;
  void cloneOrder(const Order& other);
  const Buyer& getBuyer() const;
  void setBuyer(int newBuyerId, string newBuyerName);

  int getcurrentNum() const; 
  void setOrderId(int newId);
  int getOrderId() const;

};

#endif // ORDER_H