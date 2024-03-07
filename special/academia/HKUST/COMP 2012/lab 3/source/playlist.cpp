#include "playlist.h"
#include <iostream>

PlayList::PlayList(const string& username, int capacity): username(username), capacity(capacity) {
    songs = new const Song*[capacity];  // assuming a maximum of 100 songs
    for (int i = 0; i < capacity; i++) {
        songs[i] = nullptr;
    }
}

PlayList::PlayList(const string& username, const PlayList& playlist, int capacity)
    : username{username}, songs{new Song const *[capacity]{}}, capacity{capacity} {
    // TODO 3: PlayList constructor.
    for (int idx{}; idx < capacity && idx < playlist.capacity; ++idx)
    {
        songs[idx] = playlist.songs[idx];
    }
}

PlayList::~PlayList() {
    // TODO 6: Build the destructors.
    delete[] songs;
}

void PlayList::addSong(const Song* song) {
    // TODO 4: Add and Remove Songs of a Playlist.
    for (int idx{}; idx < capacity; ++idx)
    {
        Song const *&ele{songs[idx]};
        if (!ele)
        {
            ele = song;
            break;
        }
    }
}

void PlayList::removeSong(const string& name) {
    // TODO 4: Add and Remove Songs of a Playlist.
    bool removing{};
    for (int idx{}; idx < capacity; ++idx)
    {
        Song const *&ele{songs[idx]};
        if (removing)
        {
            ele = (idx + 1) < capacity ? songs[idx + 1] : nullptr;
        }
        else if (ele && ele->getName() == name)
        {
            removing = true;
            ele = (idx + 1) < capacity ? songs[idx + 1] : nullptr;
        }
    }
}

string PlayList::getUsername() const {
    return username;
}

void PlayList::display() const {
    cout << "========================================" << endl;
    cout << "Playlist of " << username << endl;
    for (int i = 0; i < capacity; i++) {
        if (songs[i] != nullptr) {
            cout << i << ". " << songs[i]->getName() << " - " << songs[i]->getSinger()->getName() << endl;
        }
    }
    cout << "========================================" << endl;
}

