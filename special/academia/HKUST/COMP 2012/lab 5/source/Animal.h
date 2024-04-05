#include <string>
#include <iostream>
#include "FoodType.h" 

#ifndef ANIMAL_H
#define ANIMAL_H

using namespace std;

class Animal {
protected:
    string name;
    int age;
    double foodPerDay;
    FoodType foodType;
public:
    Animal(const string& name, int age, double foodPerDay, FoodType foodType);
    virtual void describe() const = 0; 
    virtual double getFoodPerDay() const { return foodPerDay; }
    FoodType getFoodType() const { return foodType; }
    virtual ~Animal() {}
};

class Carnivore : public Animal {
private:
    int teethCount; // Number of teeth
public:
    Carnivore(const string& name, int age, double foodPerDay, int teethCount);
    int getTeethCount() const { return teethCount; }
    void describe() const override;   
};

class Herbivore : public Animal {
private:
    string favoritePlant; // Favorite plant
    string habitatPreference; // Habitat
public:
    Herbivore(const string& name, int age, double foodPerDay, const string& favoritePlant, const string& habitatPreference);
    void describe() const override; 
    string getFavoritePlant() const { return favoritePlant; } 
    string getHabitatPreference() const { return habitatPreference; }   
};

#endif /* ANIMAL_H_ */
