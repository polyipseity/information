#include <iostream>
#include "manager.h"

MusicManager::MusicManager(int user_max, int singers_max, int songs_max)
    : user_list{new PlayList *[user_max]}, singer_list{new Singer *[singers_max]}, song_list{new Song *[songs_max]},
      user_capacity{user_max}, singers_capacity{singers_max}, songs_capacity{songs_max},
      num_of_user{}, num_of_singers{}, num_of_songs{} {
    // TODO 1: MusicManager constructor.
    cout << "MusicManager constructor" << endl;
}

MusicManager::~MusicManager() {
    // TODO 6: Build the destructors.
    for (int idx{}; idx < num_of_songs; ++idx)
        delete song_list[idx];
    delete[] song_list;
    for (int idx{}; idx < num_of_singers; ++idx)
        delete singer_list[idx];
    delete[] singer_list;
    for (int idx{}; idx < num_of_user; ++idx)
        delete user_list[idx];
    delete[] user_list;
    cout << "MusicManager destructor" << endl;
}

void MusicManager::createSinger(const string& name, const string& nationality) {
    singer_list[num_of_singers++] = new Singer(name, nationality);
}

void MusicManager::createSong(const string& name, const string& singer_name) {
    // TODO 2: Add a song into the MusicManager.
    if (num_of_songs >= songs_capacity)
        return;
    Singer *singer{};
    for (int idx{}; idx < num_of_singers; ++idx)
    {
        Singer *const cur{singer_list[idx]};
        if (cur->getName() == singer_name)
        {
            singer = cur;
            break;
        }
    }
    if (!singer)
        return;
    song_list[num_of_songs++] = new Song{name, singer};
}

void MusicManager::createPlaylist(const string& user_name) {
    user_list[num_of_user++] = new PlayList(user_name, MAX_SIZE);
    cout << "[Creation] Playlist of " << user_name << endl;
    // Add a new user with the given name to your data structure
    // (You can assume that the name is unique and the user list is not full.
}

void MusicManager::createPlaylistFromOther(const string& des_user_name, const string& src_user_name) {
    // TODO 5: Copy the playlist from your friend.
    if (num_of_user >= user_capacity)
        return;
    PlayList const *src{};
    for (int idx{}; idx < num_of_user; ++idx)
    {
        PlayList const *const cur{user_list[idx]};
        if (cur->getUsername() == des_user_name)
            return;
        if (cur->getUsername() == src_user_name)
            src = cur;
    }
    if (!src)
        return;
    user_list[num_of_user++] = new PlayList{des_user_name, *src};
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

