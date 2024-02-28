#include <iostream>

#include "song.h"

using namespace std;

Song::Song(const string& name, Singer* singer) : name(name), singer(singer) {
    cout << "[Creation] Song " << name << "(" << singer->getName() << ")." << endl;
}

string Song::getName() const{
    return name;
}

const Singer* Song::getSinger() const{
    return singer;
}
