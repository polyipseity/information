#ifndef LAB7_FUNCTIONS_H  
#define LAB7_FUNCTIONS_H

const int   MAX_STUDENT_NUM = 8;

struct Student {
    const char* name; // name of student
    int id;// student id
    int yearOfStudy; // year of study of the student range [1,4]
};

void print_queue(const Student* const [], int);
void get_student_data(Student* [], int);
void delete_student_record(Student* [], int);
int get_num_student(const Student* const []);
// TODOs, implement them in lab7.cpp
void reorder_student(Student* [], int);
#endif