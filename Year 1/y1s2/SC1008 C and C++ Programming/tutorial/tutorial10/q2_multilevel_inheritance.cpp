#include <iostream>
#include <string>
using namespace std;

// TODO: Update your implementation for Student Class and Person Class in Question 1
//       Declare displayInfo() as virtual

// --------------------- Person ---------------------
class Person
{
protected:
    string name;
    int age;

public:
    // constructor
    Person(string n, int a) : name(n), age(a) {}

    virtual void displayInfo() const
    {
        cout << "Name: " << name << ", Age: " << age;
    }

    virtual ~Person() = default;
};

// --------------------- Student ---------------------
class Student : public Person
{
protected:
    int studentID;

public:
    // constructor + calling parent class constructor + initialise member variable
    Student(string n, int a, int id) : Person(n, a), studentID(id) {}

    virtual void displayInfo() const
    {
        Person::displayInfo();
        cout << ", Student ID: " << studentID;
    }
};

// Derived class: GraduateStudent (inherits from Student)
class GraduateStudent : public Student
{
private:
    // TODO: Define the additional attribute (researchTopic)
    string researchTopic;

public:
    // TODO: Implement the Constructor
    GraduateStudent(string n, int a, int id, string topic) : Student(n, a, id), researchTopic(topic) {}

    // TODO: Implement displayInfo() (Note: it is virtual function in Student)
    virtual void displayInfo() const override
    {
        Student::displayInfo();
        cout << ", Research Topic: " << researchTopic;
    }
};

int main()
{
    GraduateStudent gs1("Alice", 25, 56789, "Machine Learning");
    gs1.displayInfo();
    cout << endl;

    Student *stu = &gs1;
    stu->displayInfo();
    cout << endl;

    Person *per = &gs1;
    per->displayInfo();

    return 0;
}
