#include "student.h"

// TODO 1: Implement CourseGrade::getTotalPercentage().
// Calculate the total score based on the component portions,
// i.e. total = LAB_PERCENTAGE * labs + ...
double CourseGrade::getTotalPercentage() const {
    // TODO
    return LAB_PERCENTAGE * labs + ASGN_PERCENTAGE * assignments + MIDTERM_PERCENTAGE * midtermExam + FINAL_PERCENTAGE * finalExam;
}

// Default constructor is given
Student::Student() {
    name = "";
    SID = 0;
    department = "";
    year = 0;
    grade = {0.0, 0.0, 0.0, 0.0};
}

// TODO 2: Implement Student other constructor.
// Initialize the data members with the specified parameters,
// while 'grade' is initialized to 0 similar to default constructor.
Student::Student(const string& name, int SID, const string& department, int year)
    : name{name}, SID{SID}, department{department}, year{year}, grade{}
{
    // TODO
}

// TODO 3: Implement Student mutator function.
void Student::setGrade(const CourseGrade& grade) {
    // TODO
    this->grade = grade;
}

// TODO 4: Implement Student accesor functions.
string Student::getName() const {
    // TODO
    return name;
}

int Student::getSID() const {
    // TODO
    return SID;
}

string Student::getDepartment() const {
    // TODO
    return department;
}

int Student::getYear() const {
    // TODO
    return year;
}

double Student::getTotalPercentage() const {
    // TODO
    return grade.getTotalPercentage();
}
