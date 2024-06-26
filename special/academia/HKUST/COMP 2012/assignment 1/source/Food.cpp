#include "Food.h"

// Task 2.1
Food::Food(int id, const string& name, float price) : foodID{id}, foodName{name}, price{price} {
}

// Task 2.2
Food::Food(const Food& other) : Food{other.foodID, other.foodName, other.price} {
}

// Task 2.3
void Food::setFoodId(int newId) {
  foodID = newId;
}

// Task 2.4
int Food::getFoodId() const {
  return foodID;
}

// Task 2.5
void Food::setFoodName(const string& newName) {
  foodName = newName;
}

// Task 2.6
string Food::getFoodName() const {
  return foodName;
}

// Task 2.7
void Food::setPrice(float newPrice) {
  price = newPrice;
}

// Task 2.8
float Food::getPrice() const {
  return price;
}

