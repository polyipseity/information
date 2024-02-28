#include <string>

#include "song.h"

using namespace std;

class PlayList {
private:
    string username;
    const Song** songs; // dynamic array of pointers to constant Song object
    const int capacity;
public:
    PlayList(const string& username, int capacity=100);
    PlayList(const string& username, const PlayList& playlist, int capacity=100);
    ~PlayList();
    void addSong(const Song* song);
    void removeSong(const string& name);
    string getUsername() const;
    void display() const;
};

