#ifndef __LIBRARY_H__
#define __LIBRARY_H__

#include <iostream>
#include <cstring>
using namespace std;

class Book {
    private:
        char* name;
        char* author;
        int publishYear;
    
    public:
        Book(const char* name, const char* author, int publishYear);
        ~Book();

        void printInfo() const {
            cout << name << " (" << author << ", " << publishYear << ")" << endl;
        }
};

class Bookcase {
    private:
        Book** books;
        int numBooks;
        const int capacity;
    
    public:
        Bookcase(int capacity);
        ~Bookcase();

        void addBook(const char* name, const char* author, int publishYear);

        void showContent() const {
            for (int i=0; i<numBooks; ++i) {
                books[i]->printInfo();
            }
        }
};

enum BookcaseID { SCIENCE, HUMANITIES, MISC, NUM_OF_BOOKCASES };

class Library {
    private:
        Bookcase bookcases[NUM_OF_BOOKCASES];
    
    public:
        Library(int sciCapacity, int hmnCapacity, int miscCapacity);
        ~Library();

        void addBook(const char* name, const char* author, int publishYear, BookcaseID id) {
            if (id == NUM_OF_BOOKCASES) return;
            bookcases[id].addBook(name, author, publishYear);
        }

        void showAllBooks() const {
            const char* BOOKCASE_NAMES[NUM_OF_BOOKCASES] = {"Science", "Humanities", "Misc."};
            for (int i=0; i<NUM_OF_BOOKCASES; ++i) {
                cout << "==================================" << endl;
                cout << BOOKCASE_NAMES[i] << " Category:" << endl;
                bookcases[i].showContent();
            }
        }
};

#endif // __LIBRARY_H__