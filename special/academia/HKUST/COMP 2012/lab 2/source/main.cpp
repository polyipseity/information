#include "library.h"

int main() {
    Library library{3, 4, 5};

    library.addBook("Principia Mathematica", "Isaac Newton", 1687, SCIENCE);
    library.addBook("The Success and Failure of Picasso", "John Berger", 1989, HUMANITIES);
    library.addBook("The Computer and the Brain", "John von Neumann", 1958, SCIENCE);
    library.addBook("Recipes From a 3 Star Chef", "Gordon Ramsay", 2007, MISC);

    library.showAllBooks();
    cout << endl;

    library.addBook("Mastering C++ in 3 Months", "Desmond Tsoi", 2031, SCIENCE);
    library.addBook("Bach and Mozart: Essays on the Enigma of Genius", "Robert L. Marshall", 2019, HUMANITIES);

    library.showAllBooks();
    cout << endl;

    library.addBook("Introduction to quantum mechanics, 3rd edition", "David J. Griffiths", 2018, SCIENCE);
    library.addBook("Diary of a Wimpy Kid: Big Shot", "Jeff Kinney", 2021, MISC);

    library.showAllBooks();
    cout << endl;
}