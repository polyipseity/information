#include <string>
#include <iostream>

#include "singer.h"

using namespace std;

Singer::Singer(const string& name, const string& nationality): name(name), nationality(nationality) {
    cout << "[Creation] Singer " << name << "." << endl;
}

string Singer::getName() const {
    return name;
}

string Singer::getNationality() const
{
    return nationality;
}