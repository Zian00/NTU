///////// Student Info/////////
//
//           Your Name: Zheng Mian
//      Your NTU Email: zhen0158@e.ntu.edu.sg
//
//
//
#include <iostream>

class Complex
{
private:
    double real;
    double imag;

public:
    // Constructor
    Complex(double r, double i) : real(r), imag(i) {}

    // Overloading the + operator
    // TODO: Write Your Code Here
    Complex operator+(const Complex & obj) const
    {
        double newReal = this->real + obj.real;
        double newImg = this->imag + obj.imag;
        return Complex(newReal, newImg);
    }

    // Overloading the - operator
    // TODO: Write Your Code Here
    Complex operator-(const Complex &obj) const
    {
        double newReal = this->real - obj.real;
        double newImg = this->imag - obj.imag;
        return Complex(newReal, newImg);
    }

    // Overloading the << operator for output
    friend std::ostream &operator<<(std::ostream &out, const Complex &c)
    {
        // TODO: Write Your Code Here
        if(c.imag >= 0){
            out << c.real<< " + " << c.imag << "i";
            return out;
        }
        else{
            out << c.real << " - " << (-c.imag) << "i";
            return out;
        }
        
        
    }
};

int main()
{
    Complex c1(3.5, 2.0);
    Complex c2(1.5, 4.0);

    Complex sum = c1 + c2;
    Complex diff = c1 - c2;

    std::cout << "First Complex Number: " << c1 << std::endl;
    std::cout << "Second Complex Number: " << c2 << std::endl;
    std::cout << "Sum: " << sum << std::endl;
    std::cout << "Difference: " << diff << std::endl;

    return 0;
}
