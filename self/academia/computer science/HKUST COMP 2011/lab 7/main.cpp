#include<iostream>
#include "lab7.h"

using namespace std;

int main() {
    Student* queue[MAX_STUDENT_NUM] = {nullptr};

    int reply = 0;
    int num_student = 0;
    int student_group = 0;
    // store opening
    do {
        cout << "===========================================" << endl;
        cout << "Choose what to do next:" << endl;
        cout << "1: Get student data" << endl;
        cout << "2: Reorder students" << endl;
        cout << "3: Quit" << endl;
        cin >> reply;

        switch(reply) {
        case 1:
            cin >> student_group;
            cout << "List student data: " << student_group <<endl;
            get_student_data(queue, student_group);
            num_student = get_num_student(queue);
            print_queue(queue, num_student);
            break;
        case 2:
            cout << "Start reordering students" <<endl;
            reorder_student(queue, num_student);
            print_queue(queue, num_student);
            break;
        case 3:
            cout<<"Quit program."<<endl;
            cout << "===========================================" << endl;
            break;
        default:
            delete_student_record(queue, MAX_STUDENT_NUM);
            break;
        }
    } while (reply != 3);

    return 0;
}