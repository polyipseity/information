#ifndef FOOD_H
#define FOOD_H

#include <string>
using namespace std;

class Food {
private:
    int foodID;
    string foodName;
    float price;

public:
    //Default Constructor
    Food(int id = 0, const string& name = "", float price = 0.0);
    
    // Copy constructor for Food
    Food(const Food& other);

    //Setter and getter method for Food ID
    void setFoodId(int newId);
    int getFoodId() const;
    
    //Setter and getter method for Food Name
    void setFoodName(const string& newName);
    string getFoodName() const;
    
    //Setter and getter method for Food Price
    void setPrice(float newPrice);
    float getPrice() const;
        
};

#endif // FOOD_H
