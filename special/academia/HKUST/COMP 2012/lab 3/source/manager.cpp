#include <iostream>
#include "manager.h"

MusicManager::MusicManager(int user_max, int singers_max, int songs_max) {
    // TODO 1: MusicManager constructor.
    cout << "MusicManager constructor" << endl;
}

MusicManager::~MusicManager() {
    // TODO 6: Build the destructors.
    cout << "MusicManager destructor" << endl;
}

void MusicManager::createSinger(const string& name, const string& nationality) {
    singer_list[num_of_singers++] = new Singer(name, nationality);
}

void MusicManager::createSong(const string& name, const string& singer_name) {
    // TODO 2: Add a song into the MusicManager.
}

void MusicManager::createPlaylist(const string& user_name) {
    user_list[num_of_user++] = new PlayList(user_name, MAX_SIZE);
    cout << "[Creation] Playlist of " << user_name << endl;
    // Add a new user with the given name to your data structure
    // (You can assume that the name is unique and the user list is not full.
}

void MusicManager::createPlaylistFromOther(const string& des_user_name, const string& src_user_name) {
    // TODO 5: Copy the playlist from your friend.
    cout << "[CopyCreation] Playlist of " << des_user_name << " (From:" << src_user_name << ")." << endl;
    return;
}

void MusicManager::displayPlaylist(const string& user_name) const {
    for (int i = 0; i < num_of_user; i++) {
        if (user_list[i]->getUsername() == user_name) {
            user_list[i]->display();
            return;
        }
    }
}

void MusicManager::addSongToPlaylist(const string& user_name, const string& song_name) {
    for (int i = 0; i < num_of_user; i++) {
        if (user_list[i]->getUsername() == user_name) {
            for (int j = 0; j < num_of_songs; j++) {
                if (song_list[j]->getName() == song_name) {
                    user_list[i]->addSong(song_list[j]);
                    cout << "[Add] Song " << song_list[j]->getName() << " to playlist of " << user_list[i]->getUsername() << endl;
                    return;
                }
            }
        }
    }
}

void MusicManager::removeSongFromPlaylist(const string& user_name, const string& song_name) {
    for (int i = 0; i < num_of_user; i++) {
        if (user_list[i]->getUsername() == user_name) {
            user_list[i]->removeSong(song_name);
            cout << "[Remove] Song " << song_name << " from playlist of " << user_list[i]->getUsername() << endl;
            return;
        }
    }
}

