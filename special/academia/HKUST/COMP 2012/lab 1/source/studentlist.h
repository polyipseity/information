#ifndef __STUDENTLIST_H__
#define __STUDENTLIST_H__

#include "student.h"

const int CLASS_CAPACITY = 100;
const string ALL_DEPARTMENTS = "ALL";
const int ALL_YEARS = -1;

class StudentList {
    private:
        Student students[CLASS_CAPACITY];
        int numStudents {0};

    public:
        StudentList() = default;

        void addStudent(const string& name, int SID, const string& department, int year);
        void setStudentGrade(int SID, const CourseGrade& grade);

        void displaySortedName(const string& depFilter = ALL_DEPARTMENTS, int yearFilter = ALL_YEARS) const;
        void displaySortedGrade(const string& depFilter = ALL_DEPARTMENTS, int yearFilter = ALL_YEARS) const;
};

#endif // __STUDENTLIST_H__
