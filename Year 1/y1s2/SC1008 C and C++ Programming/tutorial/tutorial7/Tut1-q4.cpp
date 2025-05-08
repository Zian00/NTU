#include <iostream>
using namespace std;

union Result
{
    int mark;
    char grade; // Can be only 'A', 'B' or 'C'
};

struct Student
{
    char studentName[50];
    bool isGrade;
    int finalMark; // Used to store the final mark
    Result res;

    void convertGrade()
    { // A=90 , B=80, C=60
        // TO-DO: Write your functions here
        if (isGrade)
        {
            switch (res.grade)
            {
            case 'A':
                finalMark = 90;
                break;
            case 'B':
                finalMark = 80;
                break;
            case 'C':
                finalMark = 60;
                break;
            default:
                finalMark = 0;
                break;
            }
        }
        else
        {
            finalMark = res.mark;
        }
    }
};

void displayStudentInfo(Student *students, int count)
{
    // TO-DO: Write your functions here
    int totalMark = 0;
    cout << "\nStudent Results:" << endl;
    for (int i = 0; i < count; i++)
    {
        cout << "Name: " << students[i].studentName << ", Final Mark: " << students[i].finalMark << endl;
        totalMark += students[i].finalMark;
    }
    float avgMark = (float)totalMark / count;
    cout << "\nAverage Final Mark: " << avgMark << endl;
}

int main()
{
    
    // TO-DO: Write your functions here
    int numOfStudents;
    cout << "How many students do you want to input?" << endl;
    cout << "Enter student size:";
    cin >> numOfStudents;
    cin.ignore();

    Student *students = new Student[numOfStudents];
    for (int i = 0; i < numOfStudents; i++)
    {
        cout << "Enter student name: ";
        cin.getline(students[i].studentName, 50);

        char resultType;
        cout << "Enter 'G' if result is grade or 'M' if result is mark:";
        cin >> resultType;
        if (resultType == 'G' || resultType == 'g')
        {
            students[i].isGrade = true;
            cout << "Enter grade (A,B,C): ";
            cin >> students[i].res.grade;
        }
        else
        {
            students[i].isGrade = false;
            cout << "Enter mark (0-100): ";
            cin >> students[i].res.mark;
        }
        cin.ignore();
        students[i].convertGrade();
    }
    displayStudentInfo(students, numOfStudents);

    delete[] students;
    students = nullptr;
    return 0;
}
