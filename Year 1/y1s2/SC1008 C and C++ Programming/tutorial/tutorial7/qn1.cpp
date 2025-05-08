/*
initial state:

int num1 = 100;
int num2 = 200;
int *p = &num1;
int &ref = *p; // ref is alias for num1
// &ref is address of ref, which is same as num1

(i). *p = 50; 
--------------
a). num1 = 50;
b). num2 = 200;
c). p = 8800;
d). *p = 50;
e). ref = 50;
f). &ref = 8800;

(ii) ref = ref / 2;
-------------------
a). num1 = 25;
b). num2 = 200;
c). p = 8800;
d). *p = 25;
e). ref = 25;
f). &ref = 8800;

(iii) p = &num2; *p = 400;
--------------------------
a). num1 = 25;
b). num2 = 400;
c). p = 9976;
d). *p = 400;
e). ref = 25; // reference is binded to num1 and cannot be changed
f). &ref = 8800; // address of reference is also binded


(iv) ref = num2; ref = ref * 2;
--------------------------
a). num1 = 400 * 2= 800;
b). num2 = 400;
c). p = 9976; (address of num2)
d). *p = 400;
e). ref = 800;  (reference to num1)
f). &ref = 8800;  (address of ref, which is the same as num1)

(v) ref = &num2;
--------------------------
a). num1 = 800;
b). num2 = 400;
c). p = 9976; (address of num2)
d). *p = 400;
e). ref = 800;  (reference to num1)
f). &ref = 8800;  (address of ref, which is the same as num1)

Error


*/

#include <iostream>
using namespace std;
int main()
{
    int num1 = 100;
    int num2 = 200;
    int *p = &num1;
    int &ref = *p;

    *p = 50;
    ref = ref / 2;
    p = &num2; *p = 400;
    ref = num2;
    ref = ref * 2;
    

    cout << "num1: " << num1 << endl;
    cout << "num2: " << num2 << endl;
    cout << "&num1: " << &num1 << endl;
    cout << "&num2: " << &num2 << endl;
    cout <<  "p: " << p << endl;
    cout << "*p: " << *p << endl;
    cout << "ref: " << ref << endl;
    cout << "&ref: " << &ref << endl; 
    return 0;
}