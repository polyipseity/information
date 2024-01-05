#include <iostream>
#include "lab7.h"
using namespace std;

// TODO: Reorder the student
// Parameters:
// <queue>: An array of pointer to <Student>s. 
// <num_stduents>: the number of students currently in the <queue>
// Task:
// Use the <yearOfStudy> member of the <Student> struct to reorder the students.
// Students at a higher year of study should be ordered in front.
// You can use bubble sort for the reordering. The detail instruction is on Lab7 webpage.
void reorder_student(Student* queue [], int num_students) {
    for (int i=0; i<num_students-1; i++) {
        for (int j=0; j<num_students-i-1; j++) {
            if (queue[j]->yearOfStudy < queue[j+1]->yearOfStudy){
                Student* temp = queue[j];
                queue[j] = queue[j+1];
                queue[j+1] = temp;
            }
        }
    }
}