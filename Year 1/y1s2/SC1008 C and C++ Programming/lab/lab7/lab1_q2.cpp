///////// Student Info/////////
//
//           Your Name: Zheng Mian
//      Your NTU Email: zhen0158@e.ntu.edu.sg
//
//
//

#include <iostream>
#include <cmath>
using namespace std;

bool isZero(float num, float epsilon = 1e-6)
{
    return fabs(num) < epsilon; // Check if num is very close to 0
}

// TO-DO: Write your code here
template <typename T>
T calculate(T num1, T num2, char operand)
{

    switch (operand)
    {
    case '+':
        return num1 + num2;
        break;
    case '-':
        return num1 - num2;

    case '*':
        return num1 * num2;

    case '/':
        if (isZero(num2))
        {
            cout << "Division by zero!\n";
            return 0;
        }
        return num1 / num2;

    default:
        return T();
    }
}

int main()
{
    cout << "Addition (10 + 5): " << calculate(10, 5, '+') << endl;
    cout << "Subtraction (10.5 - 3.2): " << calculate(10.5, 3.2, '-') << endl;
    cout << "Multiplication (4 * 2): " << calculate(4, 2, '*') << endl;
    cout << "Division (10 / 2): " << calculate(10, 2, '/') << endl;
    cout << "Division (10.6 / 0.0): " << calculate(10.6, 0.0, '/') << endl;
    cout << "Division by zero (10 / 0): " << calculate(10, 0, '/') << endl;
    return 0;
}
