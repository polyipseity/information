#ifndef BUYER_H
#define BUYER_H

#include <string>
using namespace std;

class Buyer {
private:
    int buyerID;
    string buyerName;
    
public:
    //Default Constructor
    Buyer(int id = 0, const string& name = "");

    //Setter and getter methods for Buyer ID
    int getBuyerId() const;
    void setBuyerId(int newId);

    //Setter and getter methods for Buyer Name
    string getBuyerName() const;
    void setBuyerName(const string& newName);
};

#endif // BUYER_H
