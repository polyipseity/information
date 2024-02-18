#include "studentlist.h"

// TODO 5: Implement StudentList::addStudent.
// Set the student at 'numStudents' index to a Student object with the provided parameters,
// then increment numStudents by 1.
// If there are already CLASS_CAPACITY students, this function does nothing.
// For simplicity, you don't need to handle if the name/SID already exists.
void StudentList::addStudent(const string& name, int SID, const string& department, int year) {
    // TODO
}

// TODO 6: Implement StudentList::setStudentGrade.
// Find the student whose SID is the same as the provided SID,
// and set that student's score to the provided parameter.
// For simplicity, you may assume there are no multiple students with the same SID.
void StudentList::setStudentGrade(int SID, const CourseGrade& grade) {
    // TODO
}

// Given function to print the content of the list,
// with student names sorted by alphabetic order.
// A filter is used to only print students whose department or year matches the provided filter,
// e.g. if filter is ("CSE", ALL_YEARS), only CSE students of all years of study are printed.
void StudentList::displaySortedName(const string& depFilter, int yearFilter) const {
    cout << "Name\t\tSID\t\tDep\tYr\tTotal" << endl;
    cout << "======================================================" << endl;

    Student sortedStudents[CLASS_CAPACITY];
    for (int i=0; i<numStudents; ++i) 
        sortedStudents[i] = students[i];
    for (int i=0; i<numStudents; ++i) {
        for (int j=i+1; j<numStudents; ++j) {
            if (sortedStudents[i].getName().compare(sortedStudents[j].getName()) > 0) {
                Student temp = sortedStudents[i];
                sortedStudents[i] = sortedStudents[j];
                sortedStudents[j] = temp;
            }
        }
    }

    for (int i=0; i<numStudents; ++i) {
        if ((depFilter == ALL_DEPARTMENTS || depFilter == sortedStudents[i].getDepartment())
            && (yearFilter == ALL_YEARS || yearFilter == sortedStudents[i].getYear())) {
                sortedStudents[i].display();
        }
    }
}

// TODO 7: Implement StudentList::displaySortedGrade.
// You may refer to the function above to implement this function,
// such that the students are sorted by descending total percentage score.
// Hint: only the sorting condition needs to be changed.
void StudentList::displaySortedGrade(const string& depFilter, int yearFilter) const {
    cout << "Name\t\tSID\t\tDep\tYr\tTotal" << endl;
    cout << "======================================================" << endl;

    Student sortedStudents[CLASS_CAPACITY];
    for (int i=0; i<numStudents; ++i) 
        sortedStudents[i] = students[i];
    for (int i=0; i<numStudents; ++i) {
        for (int j=i+1; j<numStudents; ++j) {
            if (false) { // TODO: add the correct swap condition here
                Student temp = sortedStudents[i];
                sortedStudents[i] = sortedStudents[j];
                sortedStudents[j] = temp;
            }
        }
    }

    for (int i=0; i<numStudents; ++i) {
        if ((depFilter == ALL_DEPARTMENTS || depFilter == sortedStudents[i].getDepartment())
            && (yearFilter == ALL_YEARS || yearFilter == sortedStudents[i].getYear())) {
                sortedStudents[i].display();
        }
    }
}