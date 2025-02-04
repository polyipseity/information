// === Region: Project Overview ===
//
//  COMP2011 Fall 2023
//  PA3: A Simplified Version of USTSPAC
//
//  Your name:
//  Your ITSC email:           @connect.ust.hk
//
//  Project TA: PAPPAS Christodoulos (cpappas@connect.ust.hk);
//              XU Shuangjie (shuangjie.xu@connect.ust.hk)
//
//  For code-level questions, please send a direct email to the above TA.
//  Asking questions with code  in a public discussion forum (e.g., Piazza) may
//  cause plagiarism issues Usually, you will get the quickest response via a
//  direct email.
//
// =====================================

// === Region: Header files ===
// Necessary header files are included,
// DO NOT include extra header files
// ============================
#include <cstring>
#include <iomanip>
#include <iostream>
using namespace std;

const int MAX_RANKING_STARS =
    5; // at most a 5-star ranking in coments (from 1-star)
const int MAX_TITLE =
    100; // at most 100 characters (including the NULL character)

// A sorted linked list of StockItem, sorted by its id
struct Student {
  unsigned int sid;     // id is an unique identifier of the Student (e.g., 39)
  char name[MAX_TITLE]; // title is a description of the Course (e.g., History)
  unsigned int ranks_count; // The total number of star_ranks on existing
                            // courses the student did until now
  Student *next;            // The pointer pointing to the next Student
};

struct StarRank {
  unsigned int star; // The star-ranking the student gave to that course
  Student *student;  // The pointer showing to the struct of the student that
                     // made the star_rank
  StarRank *next;    // The pointer pointing to the StarRanks struct
};

// A sorted linked list represents a shopping cart, sorted by item->id
struct Course {
  unsigned int course_id; // course_id is an unique identifier of the Course
                          // (e.g., History)
  char name[MAX_TITLE];   // The course name
  int stars_count[MAX_RANKING_STARS]; // The count of stars from 1 (lowest) to
                                      // MAX_RANK (highest rank) of the course
  StarRank *star_rank_head; // The pointer pointing to the StarRanks struct
};

Student *create_student(const unsigned int sid, const char name[MAX_TITLE]) {
  Student *new_student = new Student;
  new_student->sid = sid;
  strcpy(new_student->name, name);
  new_student->ranks_count = 0;
  new_student->next = nullptr;
  return new_student;
}

Course *create_course(const unsigned int course_id,
                      const char name[MAX_TITLE]) {
  Course *new_course = new Course;
  new_course->course_id = course_id;
  strcpy(new_course->name, name);
  for (int i = 0; i < MAX_RANKING_STARS; i++) {
    new_course->stars_count[i] = 0;
  }
  new_course->star_rank_head = nullptr;
  return new_course;
}

// Given the number of courses, dynamicially creates and initializes the courses
// list array
Course **dynamic_init_course_array(const unsigned int num_courses) {
  Course **ret = nullptr;
  ret = new Course *[num_courses];
  for (int i = 0; i < num_courses; i++)
    ret[i] = nullptr;
  return ret;
}

// Helper function: search student and return prev, current
// return true if found an existing entry
// return false if an existing entry is not found
bool search_student(Student *head, const unsigned int sid, Student *&prev,
                    Student *&current) {
  prev = nullptr;
  for (current = head; current != nullptr; current = current->next) {
    if (current->sid == sid) {
      // found an existing entry
      return true;
    } else if (current->sid > sid) {
      // cannot find an existing entry
      return false;
    }
    prev = current;
  }
  return false;
}

// Helper function: search star_rank and return prev, current
// return true if found an existing entry
// return false if an existing entry is not found
bool search_star_rank(StarRank *head, const unsigned int sid, StarRank *&prev,
                      StarRank *&current) {
  prev = nullptr;
  for (current = head; current != nullptr; current = current->next) {
    if (current->student->sid == sid) {
      // found an existing entry
      return true;
    }
    prev = current;
  }
  return false;
}

// Helper function: search course and return prev, current
// return true if found an existing entry
// return false if an existing entry is not found
bool search_course(Course **&course_array, const unsigned int course_id,
                   const unsigned int num_courses, int &i) {
  Course *course;
  if (course_array != nullptr) {
    for (i = 0; i < num_courses; i++) {
      course = course_array[i];
      if (course == nullptr) {
        break;
      }

      if (course->course_id == course_id) {
        // found an existing entry
        return true;
      }
    }
  }
  return false;
}

// Adds a new course in the courses array of pointers.
// If the course exists (there is a course with the course_id), return false.
// Else if the course does not exist and the array has empty space then insert
// the course and return true. Else if there is no empty space, double the array
// size (e.g., if the array has size 16, then increase it to size 32), and then
// add the course. Finally return true. The items of stars_count array of a
// newly added course must be all zero. Moreover, the star_rank_head field
// should be nullptr because there are no star ranks yet.

// @param: course_array the array of pointers for the Course
// @param: an unsigned integer representing the id of the course the student
// star ranks (course_id)
// @param: a characters array for the name of the course
// @param: an unsigned integer representing the number of courses until now.
bool add_course(Course **&course_array, const unsigned int course_id,
                const char name[MAX_TITLE], unsigned int &num_courses) {
  // found the course according to course id
  int i = 0;
  bool found_course = search_course(course_array, course_id, num_courses, i);
  if (found_course) {
    // found an existing entry
    return false; // cannot insert
  }
  // if achieve arrasy capacity
  if (i >= num_courses) {
    unsigned int new_num_courses = num_courses * 2;
    Course **course_array_new = dynamic_init_course_array(new_num_courses);
    for (int j = 0; j < num_courses; j++) {
      course_array_new[j] = course_array[j];
      course_array[j] = nullptr;
    }
    delete[] course_array;
    course_array = course_array_new;
    num_courses = new_num_courses;
    cout << "increase course array size to " << num_courses << endl;
  }
  // insert - normal case handling
  Course *new_course = create_course(course_id, name);
  course_array[i] = new_course;
  return true;
}

// Adds the star ranking of a student for a course.
// If the student or the course does not exist, return false.
// Else if the student already has a star ranking for that course then return
// return false. Else, add a star ranking, update the stars_count of the course,
// and increase by one the ranks_count of the student and return true.

// IMPORTANT: Always add in a new StarRank at the end of the list

// @param: student_head points to the head of Student list
// @param: the id of the student (sid)
// @param: course_array the array of pointers for the Course
// @param: the id of the course the student ranks (course_id)
// @param: the number of courses in the site
// @param: the rating which is a between 1 and MAX_RANKING_STARS
// @out: a boolean value indicating whether the insertion was successful
bool add_star_rank(Student *&student_head, unsigned int sid,
                   Course **&course_array, unsigned int course_id,
                   const unsigned int num_courses, int star) {
  StarRank *new_star_rank = new StarRank;

  // found the student according to sid
  Student *prev, *current;
  prev = current = nullptr;
  bool found_student = search_student(student_head, sid, prev, current);
  if (found_student) {
    // found an existing entry and point to it
    new_star_rank->student = current;
  } else {
    cout << "Failed to find student " << sid << " when add a star_rank."
         << endl;
    delete new_star_rank;
    return false;
  }

  new_star_rank->next = nullptr;
  new_star_rank->star = star;

  // found the course according to course id
  int i = 0;
  bool found_course = search_course(course_array, course_id, num_courses, i);
  if (found_course) {
    // found an existing entry and point to it
    Course *course = course_array[i];
    StarRank *star_rank_head = course->star_rank_head;
    if (star_rank_head == nullptr) {
      course->star_rank_head = new_star_rank;
    } else {
      if (star_rank_head->student->sid == sid) {
        cout << "Failed to insert star_rank because the student " << sid
             << " already have a star_rank." << endl;
        delete new_star_rank;
        return false;
      }
      while (star_rank_head->next != nullptr) {
        star_rank_head = star_rank_head->next;
        if (star_rank_head->student->sid == sid) {
          cout << "Failed to insert star_rank because the student " << sid
               << " already have a star_rank." << endl;
          delete new_star_rank;
          return false;
        }
      }
      star_rank_head->next = new_star_rank;
    }
    course->stars_count[star - 1] += 1;
  } else {
    cout << "Failed to find course " << course_id << " when add a star_rank."
         << endl;
    delete new_star_rank;
    return false;
  }

  // add student counts in the last to avoid mistake
  current->ranks_count += 1;

  return true;
}

// Adds a student to the student's linked list.
// Takes as input the student id and its name and adds the student to the list,
// in increasing order based on its student id. Note that if the student already
// exists (there is a student with the same sid), then return false. Otherwise,
// add the student (maintaining the increasing order) and return true. A new
// student always has ranks_count = 0.
bool add_student(Student *&student_head, const unsigned int sid,
                 const char name[MAX_TITLE]) {

  // empty list handling
  if (student_head == nullptr) {
    student_head = create_student(sid, name);
    return true;
  }

  Student *prev, *current;
  prev = current = nullptr;
  bool found_student = search_student(student_head, sid, prev, current);

  if (found_student) {
    // found an existing entry
    return false; // cannot insert
  }

  // insert - normal case handling
  Student *new_student = create_student(sid, name);
  if (prev == nullptr) {
    // insert to the front
    new_student->next = student_head;
    student_head = new_student;
  } else {
    prev->next = new_student;
    new_student->next = current;
  }
  return true;
}

// Removes the star ranking of a student for a course.
// If the star ranking does not exist, return false.
// Else, delete the star ranking, decrease the ranks_count of the student with
// id sid, and
// update the new stars_count of the course with id course_id. Finally return
// true.

// @param: student_head points to the head of Student list
// @param: course_array the array of pointers for the Course
// @param: the id of the student (sid)
// @param: the id of the course the student ranks (course_id)
// @param: the number of courses in the site
// @out: a boolean value indicating whether the removal was successful
bool delete_star_rank(Student *&student_head, Course **&course_array,
                      const unsigned int sid, const unsigned int course_id,
                      const unsigned int num_courses) {
  // search course containing this star_rank
  int i = 0;
  bool found_course = search_course(course_array, course_id, num_courses, i);
  if (found_course == false) {
    cout << "Failed to delete star_rank, course " << course_id << " not found."
         << endl;
    return false;
  }
  // alse need to delete coments in course
  StarRank *prev, *current;
  prev = current = nullptr;
  bool found_star_rank =
      search_star_rank(course_array[i]->star_rank_head, sid, prev, current);
  if (found_star_rank == false) {
    cout << "Failed to delete star_rank, star_rank not found in course "
         << course_id << endl;
    return false;
  }

  // update student star_rank_count
  current->student->ranks_count -= 1;

  // update course star array
  course_array[i]->stars_count[current->star - 1] -= 1;

  // found an existing entry and delete this pointer
  if (prev == nullptr) {
    // delete and update the head
    course_array[i]->star_rank_head = current->next;
    delete current;
  } else {
    prev->next = current->next;
    delete current;
  }
  return true;
}

// Takes as input a course_id and deletes the corresponding course.
// If the course does not exist, return false.
// Else if there are any star ranks, delete them, decrease the ranks_count of
// the corresponding students, and delete the course. Return true. If the course
// array has a size of N and N/2 entries are empty, decrease the array size by
// half (while maintaining the courses). Return true.

// ****IMPORTANT Notes****
// 1) Whenever you delete a class, you need to swap all the classes
// in the right of that class, one step left.
// For example, if we remove C4 from the array:
// [C1,C2,C3,C4,C5,C6,nullptr,nullptr]
// Then the resulting array will be:
// [C1,C2,C3,C5,C6,nullptr,nullptr,nullptr]

// 2) The minimum size of the array is 2.
// You MUST NOT reduce the size of the array to 1.

// @param: student_head points to the head of Student list
// @param: course_array the array of pointers for the Course
// @param: the id of the course the student ranks (course_id)
// @param: the number of courses in the site
// @out: a boolean value indicating whether the removal was successful
bool delete_course(Student *student_head, Course **&course_array,
                   const unsigned int course_id, unsigned int &num_courses) {
  // found the course according to course id
  int i = 0;
  bool found_course = search_course(course_array, course_id, num_courses, i);
  if (found_course == false) {
    cout << "Failed to delete course, course " << course_id << " not found."
         << endl;
    return false;
  }

  // delete all star_rank
  StarRank *current;
  StarRank *star_rank_head = course_array[i]->star_rank_head;
  if (star_rank_head != nullptr) {
    for (; star_rank_head->next != nullptr;) {
      delete_star_rank(student_head, course_array,
                       star_rank_head->next->student->sid, course_id,
                       num_courses);
    }
    delete_star_rank(student_head, course_array, star_rank_head->student->sid,
                     course_id, num_courses);
  }

  delete course_array[i];

  // need to move items after delete one ahead
  unsigned int count_valid = 0;
  for (unsigned int j = i; j < num_courses - 1; j++) {
    course_array[j] = course_array[j + 1];
    count_valid = j;
    if (course_array[j] == nullptr) {
      break;
    }
    count_valid += 1;
  }
  course_array[num_courses - 1] = nullptr;

  // reconstruct array when number is small
  unsigned int new_num_courses = (num_courses + 1) / 2;
  if (count_valid > new_num_courses)
    return true; // no need reduce size
  if (new_num_courses < 2)
    return true;

  Course **course_array_new = dynamic_init_course_array(new_num_courses);
  for (int j = 0; j < new_num_courses; j++) {
    course_array_new[j] = course_array[j];
    course_array[j] = nullptr;
  }
  delete[] course_array;
  course_array = course_array_new;
  num_courses = new_num_courses;
  cout << "reduce course array size to " << num_courses << endl;
  return true;
}

// unsigned int new_num_courses = num_courses * 2;
// Course **course_array_new = dynamic_init_course_array(new_num_courses);
// for (int j = 0; j < num_courses; j++) {
//   course_array_new[j] = course_array[j];
//   course_array[j] = nullptr;
// }
// delete[] course_array;
// course_array = course_array_new;
// num_courses = new_num_courses;
// cout << "increase course array size to " << num_courses << endl;

void clean_up(Student *&student_head, StarRank *&star_rank_head,
              Course **&course_array, unsigned int &num_courses) {
  // delete all courses, be carefully for the memory leak
  while (course_array[0] != nullptr) {
    delete_course(student_head, course_array, course_array[0]->course_id,
                  num_courses);
  }

  if (student_head != nullptr) {
    Student *student;
    while (student_head->next != nullptr) {
      // remove student, need first delete all the star_rank of this student,
      // and then delete star_ranks in course remove_student(student_head,
      // star_rank_head, student_head->sid);
      student = student_head->next;
      student_head->next = student_head->next->next;
      delete student;
    }
    delete student_head;
    student_head = nullptr;
  }

  delete[] course_array; // delete the dynamically allocated 2D array
  course_array = nullptr;
}

// Display the data of all students in increasing order of their sid in the
// form:
// === Student List ([sid, name, ranks_count]) ===
// [sid, name and ranks_count] -> [...] -> ... -> [...]
// @param: student_head points to the head of Student list
void display_students(Student *student_head) {
  // Write the code to display students
  const Student *student;
  int count = 0;

  cout << "=== Student List ([sid, name, star_rank count]) ===" << endl;
  for (student = student_head; student != nullptr; student = student->next) {
    cout << "[" << student->sid << ", " << student->name << ", "
         << student->ranks_count << "]";
    if (student->next != nullptr)
      cout << " -> ";
    count++;
  }
  if (count == 0) {
    cout << "No items in the Student list" << endl;
  } else {
    cout << endl;
  }
}

// Display star ranks of the course given its id.
// In the form:
// star_ranks in course _COURSE_NAME_ : [star ranker sid : star] -> [...]

// @param: course_array the array of pointers for the Course
// @param: the number of courses in the site
// @param: the id of the course
void display_star_ranks(Course **course_array, const unsigned int num_courses,
                        const unsigned int course_id) {
  const Student *student;
  const StarRank *star_rank;
  const Course *course;
  int count, count_star_rank, i;

  if (course_array != nullptr) {
    for (int i = 0; i < num_courses; i++) {
      count = 0;
      course = course_array[i];
      if (course == nullptr) {
        break;
      }

      if (course->course_id == course_id) {
        count_star_rank = 0;
        cout << "star_ranks in course " << course->name << " : ";
        for (star_rank = course->star_rank_head; star_rank != nullptr;
             star_rank = star_rank->next) {
          if (star_rank != nullptr) {
            cout << "[" << star_rank->student->sid << ": " << star_rank->star
                 << "]";
            if (star_rank->next != nullptr)
              cout << " -> "; // except the last item, print a comma
            count_star_rank++;
          }
        }
        if (count_star_rank == 0) {
          cout << "No StarRanks in the course " << course->name << endl;
        } else {
          cout << endl;
        }
        return;
      }
    }
    cout << "Course not found " << endl;
  }
}

// Display all existing courses. For each course display its name and its
// star-ranking array in the form:
// course_id : _COURSE_ID_, name : _COURSE_NAME, stars_count:
//*     _one_star
//**    _two_stars
//***   _three_stars
//****  _four_stars
//***** _five_stars
// @param: course_array the array of pointers for the Course
// @param: the number of courses in the site
void display_courses(Course **course_array, const unsigned int num_courses) {
  const Student *student;
  const StarRank *star_rank;
  const Course *course;
  int count, count_star_rank, i;

  if (course_array != nullptr) {
    count = 0;
    for (i = 0; i < num_courses; i++) {
      course = course_array[i];
      if (course == nullptr) {
        continue;
      }

      cout << "course_id : " << course->course_id << ", name : " << course->name
           << ", stars_count : " << endl;

      for (int star_id = 0; star_id < MAX_RANKING_STARS; star_id++) {
        for (int j = 0; j < star_id + 1; j++) {
          cout << "*";
        }
        for (int k = 0; k < MAX_RANKING_STARS - star_id; k++) {
          cout << " ";
        }
        cout << course->stars_count[star_id] << endl;
      }

      count++;
    }
    if (count == 0) {
      cout << "No course in the list " << endl;
    }
  }
}

// === Region: The main function ===
// The main function implementation is given
// DO NOT make any changes to the main function
// ============================
int main() {
  enum MeunOption {
    OPTION_DISPLAY_STUDENT_LIST = 0,
    OPTION_DISPLAY_COURSES,
    OPTION_DISPLAY_COMMENTS,
    // OPTION_DISPLAY_CURRENT_LIST,
    OPTION_INSERT_STUDENT,
    OPTION_INSERT_COURSE,
    OPTION_INSERT_COMMENT,
    OPTION_DELETE_COMMENT,
    OPTION_DELETE_COURSE,
    OPTION_EXIT_SYSTEM,
    MAX_MENU_OPTIONS
  };
  const int MAX_MENU_OPTIONS_LENGTH = 80;
  char menu_options[MAX_MENU_OPTIONS][MAX_MENU_OPTIONS_LENGTH] = {
      "Display student list",
      "Display courses",
      "Display star_ranks of course ",
      "Insert a new student to the student list",
      "Insert a new course to the course list",
      "Insert a new star_rank to the star_rank list",
      "Delete a star_rank by student id and course id",
      "Delete a course by course id",
      "Exit the system"};

  Student *student_head = nullptr;
  StarRank *star_rank_head = nullptr;
  Course **course_array = nullptr;
  unsigned int num_courses = 0;
  int i, option;
  unsigned int sid, course_id, star;
  char name[MAX_TITLE] = "";
  bool ret = false;

  num_courses = 2;
  course_array = dynamic_init_course_array(num_courses);

  cout << "=== Simplified USTSPAC System ===" << endl;
  while (true) {
    cout << "=== Menu ===" << endl;
    for (i = 0; i < MAX_MENU_OPTIONS; i++)
      cout << i + 1 << ": " << menu_options[i]
           << endl; // shift by +1 when display

    cout << "Enter your option: " << endl;
    cin >> option;
    option = option - 1; // shift by -1 after entering the option

    // The invalid menu option handling
    if (option < 0 || option >= MAX_MENU_OPTIONS) {
      cout << "Invalid option" << endl;
      continue;
    }

    // Exit operations handling
    if (option == OPTION_EXIT_SYSTEM) {
      clean_up(student_head, star_rank_head, course_array, num_courses);
      break; // break the while loop
    }

    switch (option) {
    case OPTION_DISPLAY_STUDENT_LIST:
      display_students(student_head);
      break;
    case OPTION_DISPLAY_COURSES:
      display_courses(course_array, num_courses);
      break;
    case OPTION_DISPLAY_COMMENTS:
      course_id = 0;
      cout << "Enter the course id: " << endl;
      cin >> course_id;
      if (course_id <= 0) {
        cout << "Enter a valid course id > 0" << endl;
        break;
      }
      display_star_ranks(course_array, num_courses, course_id);

      break;
    case OPTION_INSERT_STUDENT:
      sid = 0;
      cout << "Enter the student id: " << endl;
      cin >> sid;
      if (sid <= 0) {
        cout << "Enter a valid student id > 0" << endl;
        break;
      }
      cout << "Enter a name: " << endl;
      cin >> name;

      ret = add_student(student_head, sid, name);
      if (ret == false) {
        cout << "Failed to insert student " << sid << endl;
      } else {
        cout << sid << " is successfully inserted" << endl;
      }
      break;
    case OPTION_INSERT_COURSE:
      course_id = 0;
      cout << "Enter the course id: " << endl;
      cin >> course_id;
      if (course_id <= 0) {
        cout << "Enter a valid course id > 0" << endl;
        break;
      }
      cout << "Enter a name: " << endl;
      cin >> name;

      ret = add_course(course_array, course_id, name, num_courses);
      if (ret == false) {
        cout << "Failed to insert course " << course_id << endl;
      } else {
        cout << course_id << " is successfully inserted" << endl;
      }
      break;
    case OPTION_INSERT_COMMENT:
      sid = 0;
      cout << "Enter the student id: " << endl;
      cin >> sid;
      if (sid <= 0) {
        cout << "Enter a valid student id > 0" << endl;
        break;
      }
      course_id = 0;
      cout << "Enter the course id: " << endl;
      cin >> course_id;
      if (course_id <= 0) {
        cout << "Enter a valid course id > 0" << endl;
        break;
      }
      star = 0;
      cout << "Enter the star rank of this course: " << endl;
      cin >> star;
      if (star <= 0 || star > MAX_RANKING_STARS) {
        cout << "Enter a valid course id > 0 && < " << MAX_RANKING_STARS
             << endl;
        break;
      }

      ret = add_star_rank(student_head, sid, course_array, course_id,
                          num_courses, star);
      if (ret == false) {
        cout << "Failed to insert star_rank, sid: " << sid
             << ", course id: " << course_id << endl;
      } else {
        cout << " star_rank is successfully inserted" << endl;
      }
      break;
    case OPTION_DELETE_COMMENT:
      sid = 0;
      cout << "Enter the student id: " << endl;
      cin >> sid;
      if (sid <= 0) {
        cout << "Enter a valid student id > 0" << endl;
        break;
      }
      course_id = 0;
      cout << "Enter the course id: " << endl;
      cin >> course_id;
      if (course_id <= 0) {
        cout << "Enter a valid course id > 0" << endl;
        break;
      }

      ret = delete_star_rank(student_head, course_array, sid, course_id,
                             num_courses);
      if (ret == false) {
        cout << "Failed to delete star_rank, sid: " << sid
             << ", course id: " << course_id << endl;
      } else {
        cout << " star_rank is successfully deleted" << endl;
      }
      break;
    case OPTION_DELETE_COURSE:
      course_id = 0;
      cout << "Enter the course id: " << endl;
      cin >> course_id;
      if (course_id <= 0) {
        cout << "Enter a valid course id > 0" << endl;
        break;
      }

      ret = delete_course(student_head, course_array, course_id, num_courses);
      if (ret == false) {
        cout << "Failed to delete course, course id: " << course_id << endl;
      } else {
        cout << "course is successfully deleted" << endl;
      }
      break;
    default:
      break;
    } // end of switch (option)
  }

  return 0;
}