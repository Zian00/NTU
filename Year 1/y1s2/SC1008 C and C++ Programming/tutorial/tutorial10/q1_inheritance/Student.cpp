#include "Student.h"
#include <iostream>
using namespace std;

// TODO: Implement Student class constructor and initialize studentID
Student::Student(string n, int a, int id) : Person(n, a), studentID(id) {}

void Student::displayInfo() const
{
    // TODO: Output Student Information
    cout << "Name: " << name << ", Age: " << age << '\n'
         << "Student ID: " << studentID << '\n';
}