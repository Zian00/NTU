#pragma once
#ifndef PERSON_H
#define PERSON_H

#include <string>
using namespace std;

class Person {
protected:
    string name;
    int age;

public:
    Person(string n, int a);
    void displayInfo() const;
};

#endif // PERSON_H