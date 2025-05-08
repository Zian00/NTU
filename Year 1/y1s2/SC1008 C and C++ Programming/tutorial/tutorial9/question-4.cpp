#include <iostream>

class Box
{
private:
    double length;
    double width;
    double height;

public:
    // Constructor to initialize the box dimensions
    Box(double l, double w, double h)
    {
        length = l;
        width = w;
        height = h;
    }

    // Member function that can access the private members
    void calculateVolume()
    {
        // Caclulate and display the volume of the box
        // TODO: Write your code here
        double volume = this->length * this->width * this->height;
        std::cout << "Box Volume: " << volume << " cubic units" << std::endl;
    }

    // Declare a friend function to display private members
    // TODO: Write your code here
    friend void displayDimensions(const Box& obj);
};

// Define the friend function (that can access private members of Box)
// TODO: Write your code here
void displayDimensions(const Box& obj)
{
    std::cout << "Box Dimensions: " << std::endl;
    std::cout << "Length: " << obj.length << std::endl;
    std::cout << "Width: " << obj.width << std::endl;
    std::cout << "Height: " << obj.height << std::endl;
    std::cout << std::endl;
}

int main()
{
    // Creating a Box object
    Box myBox(5.0, 3.0, 2.0);

    // Friend function accessing private data
    displayDimensions(myBox);

    // Member function accessing private data
    myBox.calculateVolume();

    return 0;
}
