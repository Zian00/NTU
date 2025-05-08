///////// Student Info/////////
//
//           Your Name: Zheng Mian
//      Your NTU Email: zhen0158@e.ntu.edu.sg
//
//
//

#include <iostream>
#include <cstring>
#include <limits>
using namespace std;

// Function to get a valid integer input
int getValidInt()
{
    // TO-DO: Write your code here
    int userInputInt;
    while (true)
    {
        cin >> userInputInt;
        if (cin.fail())
        {
            cin.clear();                                         // Clear error state
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
            cout << "Invalid input! Please enter a valid integer: ";
        }
        else
        {
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return userInputInt;
        }
    }
}

// Function to get a valid float input
float getValidFloat()
{

    // TO-DO: Write your code here
    float userInputFloat;

    while (true)
    {
        cin >> userInputFloat;
        if (cin.fail())
        {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Invalid input! Please enter a valid float number: ";
        }
        else
        {
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return userInputFloat;
        }
    }
}

int main()
{
    char name[50];  // Student name
    int studentID;  // Student ID
    float mathMark; // Math mark

    while (true)
    {
        // Get student name
        cout << "Enter student name (or enter '#' to exit): ";
        cin.getline(name, 50);

        // Check if user wants to exit
        if (strcmp(name, "#") == 0)
        {
            break;
        }

        // Get student ID
        cout << "Enter student ID (integer): ";
        studentID = getValidInt();

        // Get math mark
        cout << "Enter math mark (float): ";
        mathMark = getValidFloat();

        // Display student information
        cout << "\nStudent Information:\n";
        cout << "Name: " << name << endl;
        cout << "Student ID: " << studentID << endl;
        cout << "Math Mark: " << mathMark << endl;
        cout << "-------------------------\n";
    }

    cout << "Program exited successfully." << endl;
    return 0;
}
