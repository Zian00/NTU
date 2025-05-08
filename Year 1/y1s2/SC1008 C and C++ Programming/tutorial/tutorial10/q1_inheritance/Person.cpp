#include "Person.h"
#include <iostream>
using namespace std;

// TODO: Implement Person class constructor and function here
Person::Person(string n, int a) : name(n), age(a) {
    // TODO: Initialize member variables

}

void Person::displayInfo() const {
    // TODO: Display person's details
    cout<<"Name: " << name << ", Age: " << age<<endl;
}