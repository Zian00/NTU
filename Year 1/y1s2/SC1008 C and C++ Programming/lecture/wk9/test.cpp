#include <iostream>
using namespace std;
void modifyPointer(int *p)
{
    int x = 10;
    p = &x; // This only modifies the local copy of pointer p, not the original pointer p in main
}
int main()
{
    int a = 5;
    int *ptr = &a;
    cout << "Before modifyPointer: " << *ptr << endl;
    modifyPointer(ptr);
    cout << "After modifyPointer : " << *ptr << endl; // Still 5
    return 0;
}