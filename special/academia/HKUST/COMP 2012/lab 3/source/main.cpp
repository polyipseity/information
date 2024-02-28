# include <iostream>
# include "manager.h"

using namespace std;


int main() {

    MusicManager manager(100, 100, 100);

    // create singers
    manager.createSinger("Adele", "British");
    manager.createSinger("Taylor Swift", "American");
    manager.createSinger("Jay Chou", "Chinese");

    // create songs
    manager.createSong("Hello", "Adele");
    manager.createSong("Rolling in the Deep", "Adele");
    manager.createSong("Someone Like You", "Adele");
    manager.createSong("Shake It Off", "Taylor Swift");
    manager.createSong("Blank Space", "Taylor Swift");
    manager.createSong("Love Story", "Taylor Swift");
    manager.createSong("Mojito", "Jay Chou");
    manager.createSong("Love Confession", "Jay Chou");
    manager.createSong("Simple Love", "Jay Chou");

    // create users and playlist
    manager.createPlaylist("Desmond");

    // add songs to playlist
    manager.addSongToPlaylist("Desmond", "Hello");
    manager.addSongToPlaylist("Desmond", "Shake It Off");
    manager.addSongToPlaylist("Desmond", "Love Story");
    manager.addSongToPlaylist("Desmond", "Mojito");

    // create users and copy playlist from other user
    manager.createPlaylistFromOther("Cecia", "Desmond");

    // add songs to playlist
    manager.addSongToPlaylist("Cecia", "Rolling in the Deep");
    manager.addSongToPlaylist("Cecia", "Blank Space");
    manager.addSongToPlaylist("Cecia", "Someone Like You");
    manager.removeSongFromPlaylist("Cecia", "Shake It Off");
    manager.removeSongFromPlaylist("Cecia", "Love Story");

    // display playlist
    manager.displayPlaylist("Desmond");
    manager.displayPlaylist("Cecia");

}

