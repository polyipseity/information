#ifndef __STUDENT_H__
#define __STUDENT_H__

#include <iostream>
#include <string>
using namespace std;

const int LAB_PERCENTAGE = 10;
const int ASGN_PERCENTAGE = 24;
const int MIDTERM_PERCENTAGE = 26;
const int FINAL_PERCENTAGE = 40;

struct CourseGrade {
    double labs;
    double assignments;
    double midtermExam;
    double finalExam;

    double getTotalPercentage() const;
};

class Student {
    private:
        string name;
        int SID;
        string department;
        int year;
        CourseGrade grade;

    public:
        Student();
        Student(const string& name, int SID, const string& department, int year);

        void setGrade(const CourseGrade& grade);

        string getName() const; 
        int getSID() const;
        string getDepartment() const;
        int getYear() const;
        double getTotalPercentage() const;

        void display() const {
            cout << name << "\t\t" << SID << "\t" << department << "\t" << year << "\t" << grade.getTotalPercentage() << endl;
        }
};

#endif // __STUDENT_H__
