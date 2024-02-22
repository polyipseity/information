#include "library.h"

Book::Book(const char* name, const char* author, int publishYear) {
    // TODO 1: Book constructor
}

Book::~Book() {
    // TODO 2: Book destructor
}

Bookcase::Bookcase(int capacity) {
    // TODO 3: Bookcase constructor
    // Initialize books to an array of length 'capacity', and numBooks to 0.
    // Hint: how to initialize constant data member capacity?
}

Bookcase::~Bookcase() {
    // TODO 4: Bookcase destructor
}

void Bookcase::addBook(const char* name, const char* author, int publishYear) {
    if (false) { // TODO 5.1: full condition
        cout << "Bookcase is full, cannot add " << name << "!" << endl;
        return;
    }

    // TODO 5.2: add a new Book to the books array at index numBooks, then increment numBooks.
}

Library::Library(int sciCapacity, int hmnCapacity, int miscCapacity) {
    // TODO 6: Library constructor
    // Hint: Bookcase has no default constructor. How to initialize bookcases?
}

Library::~Library() {
    // TODO 7: Library destructor
    // Hint: Anything to delete?
}
