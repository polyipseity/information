#include <iostream>
#include "studentlist.h"
using namespace std;

int main() {
    StudentList comp2012;
    comp2012.addStudent("Alice", 20123456, "CSE", 2);
    comp2012.addStudent("Bob", 20234567, "ECE", 2);
    comp2012.addStudent("Charles", 20345678, "MATH", 3);
    comp2012.addStudent("Danny", 20456789, "CSE", 3);
    comp2012.addStudent("Evan", 20567890, "PHYS", 1);
    comp2012.addStudent("Francis", 20678901, "CSE", 2);
    comp2012.addStudent("Gerald", 20789012, "MATH", 4);
    comp2012.addStudent("Harry", 20890123, "CSE", 2);

    comp2012.setStudentGrade(20123456, {1.0, 0.7, 0.9, 0.8});
    comp2012.setStudentGrade(20234567, {0.9, 0.9, 0.65, 0.75});
    comp2012.setStudentGrade(20345678, {1.0, 0.8, 0.7, 0.75});
    comp2012.setStudentGrade(20456789, {0.6, 0.5, 0.45, 0.7});
    comp2012.setStudentGrade(20567890, {0.8, 0.65, 0.85, 0.65});
    comp2012.setStudentGrade(20678901, {1.0, 1.0, 0.9, 0.9});
    comp2012.setStudentGrade(20789012, {1.0, 0.4, 0.6, 0.75});
    comp2012.setStudentGrade(20890123, {0.0, 0.5, 0.75, 0.5});

    cout << "Viewing all students sorted by name: " << endl << endl;
    comp2012.displaySortedName();
    cout << endl;

    cout << "Viewing all CSE students sorted by name: " << endl << endl;
    comp2012.displaySortedName("CSE", ALL_YEARS);
    cout << endl;

    cout << "Viewing all year 2 students sorted by name: " << endl << endl;
    comp2012.displaySortedName(ALL_DEPARTMENTS, 2);
    cout << endl;

    cout << "Viewing all students sorted by grade: " << endl << endl;
    comp2012.displaySortedGrade();
    cout << endl;

    cout << "Viewing all year 2 CSE students sorted by grade: " << endl << endl;
    comp2012.displaySortedGrade("CSE", 2);
    cout << endl;
}