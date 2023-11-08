#include <iostream>
#include "lab7.h"

using namespace std;

// print out the information of students
void print_queue(const Student* const queue[], int num_student) {
    for (int i=0; i<num_student; ++i) {
        if (queue[i]==nullptr) {
            break;
        }
        const Student* cur_student = queue[i];
        cout << "Student Name: "  << cur_student->name << ", ID: " << cur_student->id;
        cout << ", YearOfStudy: Year " << cur_student->yearOfStudy<<endl;
    }
}

// clear the pointer array
void delete_student_record(Student* queue[], int num_student) {
    for (int i=0; i<num_student; ++i) {
        delete queue[i];
        queue[i] = nullptr;
    }
}

//Student data for different testcases
void get_student_data(Student* queue[], int student_array_id){
    if(student_array_id<=0 or student_array_id >5){
        cout<<"not valid student array id"<<endl;
    }
    for (int i=0; i<MAX_STUDENT_NUM; ++i) {
        if (queue[i]!=nullptr) {
            delete queue[i];
            queue[i] = nullptr;
        }
    }
    switch (student_array_id){
        case 1:
            queue[0] = new Student{"Amy    ", 1, 4};
            queue[1] = new Student{"Bob    ", 2, 2};
            queue[2] = new Student{"Charlie", 3, 3};
            queue[3] = new Student{"Dan    ", 4, 1};
            queue[4] = new Student{"Emily  ", 5, 2};
            queue[5] = new Student{"Frank  ", 6, 4};
            queue[6] = new Student{"George ", 7, 3};
            queue[7] = new Student{"Hans   ", 8, 3};
            break;
        case 2:
            queue[0] = new Student{"Mary   ", 1, 2};
            queue[1] = new Student{"Tony   ", 2, 3};
            queue[2] = new Student{"Charles", 3, 4};
            break;
        case 3:
            queue[0] = new Student{"Leon   ", 1, 1};
            break;
        case 4:
            queue[0] = new Student{"Kai    ", 1, 4};
            queue[1] = new Student{"Julian ", 2, 4};
            queue[2] = new Student{"Jack   ", 3, 4};
            queue[3] = new Student{"Dean   ", 4, 4};
            break;
        case 5:
            queue[0] = new Student{"Richard", 1, 4};
            queue[1] = new Student{"Ian    ", 2, 4};
            queue[2] = new Student{"Ollie  ", 3, 3};
            queue[3] = new Student{"Tony   ", 4, 3};
            queue[4] = new Student{"William", 5, 2};
            queue[5] = new Student{"Penny  ", 6, 1};
            queue[6] = new Student{"Gia    ", 7, 1};
            break;
        default:
            break;
    }
}

// get number of students (not null pointer)
int get_num_student(const Student* const queue[]){
    int num_student = 0;
    for(int i = 0; i < MAX_STUDENT_NUM;i++){
        if(queue[i]!= nullptr)
            num_student++;
    }
    return num_student;
}