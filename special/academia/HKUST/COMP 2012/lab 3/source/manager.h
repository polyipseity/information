#include <string>

#include "playlist.h"

using namespace std;

const int MAX_SIZE = 100;

class MusicManager {
private:
    PlayList** user_list; // dynamic array of pointers to PlayList object
    Singer** singer_list; // dynamic array of pointers to Singer object
    Song** song_list; // dynamic array of pointers to Song object
    const int user_capacity, singers_capacity, songs_capacity;
    int num_of_user, num_of_singers, num_of_songs;

public:
    MusicManager(int user_max, int singers_max, int songs_max);
    ~MusicManager();
    void createSinger(const string& name, const string& nationality);
    void createSong(const string& name, const string& singer_name);
    void createPlaylist(const string& user_name);
    void createPlaylistFromOther(const string& des_user_name, const string& src_user_name);
    void displayPlaylist(const string& user_name) const;
    void addSongToPlaylist(const string& user_name, const string& song_name);
    void removeSongFromPlaylist(const string& user_name, const string& song_name);
};

