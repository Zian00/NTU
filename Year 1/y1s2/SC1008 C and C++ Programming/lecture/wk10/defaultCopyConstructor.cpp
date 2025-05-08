#include <iostream>
class MyClass
{
public:
    MyClass();
    MyClass(int a);
    // No user-defined copy constructor here

    ~MyClass()
    {
        std::cout << "Bye!" << data << std::endl;
    }
    void doSomething();

private:
    int data;
};
MyClass::MyClass() { data = 0; }
MyClass::MyClass(int a)
{
    data = a;
}
void MyClass::doSomething()
{
    std::cout << "Do something!"
              << std::endl;
}
int main()
{
    MyClass toyClass1(10);
    MyClass toyClass2 = toyClass1;
    MyClass toyClass3(toyClass1);
}