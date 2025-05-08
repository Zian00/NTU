#include <iostream>
using namespace std;
class MyClass
{
private:
    int value;

public:
    MyClass(int v) { value = v; } // Constructor
    // Overloading the + operator
    MyClass operator+(const MyClass &obj) const
    {
        return MyClass(value + obj.value);
    }
    // Function sum() that does the same as operator+
    MyClass sum(const MyClass &obj) const
    {
        return MyClass(value + obj.value);
    }

    void display() { cout << "Value : " << value << endl; }
};
int main()
{
    MyClass obj1(10), obj2(20);
    MyClass obj3 = obj1 + obj2; // Using overloaded + operator
    obj3.display();
    MyClass obj4 = obj1.sum(obj2); // Using sum() function
    obj4.display();
    return 0;
}