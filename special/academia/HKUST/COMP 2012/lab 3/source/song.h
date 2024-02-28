#include <string>

#include "singer.h"

using namespace std;

class Song {
    private:
        string name;
        Singer* singer;
    public:
        Song(const string& name, Singer* singer);
        Song(const Song&) = delete;
        string getName() const;
        const Singer* getSinger() const;
};

