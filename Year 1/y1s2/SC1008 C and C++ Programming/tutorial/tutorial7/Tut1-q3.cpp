#include <iostream>
using namespace std;

// TO-DO: Write your functions here
template <typename T>
T calArea(T length1, T width=0, T height =0 ){
    if (width == 0 && height == 0) {
        return length1 * length1;
    }

    else if (height ==0){
        return length1 * width;
    }
    else{
        return 0.5f * (length1 + width) * height;
    }
}



int main() {
    // Test cases
    int side1 = 5;
    cout << "Area of Square: " << calArea(side1) << endl;
    double side2 = 11.11;
    cout << "Area of Square: " << calArea(side2) << endl;

    int length1 = 10, width1 = 20;
    cout << "Area of Rectangle: " << calArea(length1, width1) << endl;
    float length2 = 23.4, width2 = 10.8;
    cout << "Area of Rectangle: " << calArea(length2, width2) << endl;

    long b1 = 20, b2 = 40, height = 10; 
    cout << "Area of Trapezoid: " << calArea(b1, b2, height) << endl;

    return 0;
}
