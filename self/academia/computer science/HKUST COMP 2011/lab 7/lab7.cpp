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
void reorder_student(Student *queue[], int num_students)
{
  if (num_students <= 1)
  {
    return;
  }
  int const mid{num_students / 2};
  Student **const queue_mid{&queue[mid]}, *const *const queue_end{&queue[num_students]};
  reorder_student(queue, mid);
  reorder_student(queue_mid, num_students - mid);
  Student *const *left_iter{queue}, *const *right_iter{queue_mid}, **tmp{new Student *[num_students]};
  for (int ii{}; ii < num_students; ++ii)
  {
    tmp[ii] = left_iter == queue_mid || right_iter != queue_end && (*right_iter)->yearOfStudy > (*left_iter)->yearOfStudy ? *right_iter++ : *left_iter++;
  }
  for (int ii{}; ii < num_students; ++ii)
  {
    queue[ii] = tmp[ii];
  }
  delete[] tmp;
}
