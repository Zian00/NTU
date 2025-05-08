#include <stdio.h>

int main()
{
    /* Write your code here */
    int studentId, marks;

    while (1)
    {
        printf("Enter Student ID:\n");
        scanf("%d", &studentId);
        if (studentId == -1)
        {
            break;
        }

        printf("Enter Mark:\n");
        scanf("%d", &marks);
        if (marks <= 100 && marks >= 75)
        {
            printf("Grade = A\n");
        }
        else if (marks <= 74 && marks >= 65)
        {
            printf("Grade = B\n");
        }
        else if (marks <= 64 && marks >= 55)
        {
            printf("Grade = C\n");
        }
        else if (marks <= 54 && marks >= 45)
        {
            printf("Grade = D\n");
        }
        else if (marks <= 44 && marks >= 0)
        {
            printf("Grade = F\n");
        }
    }
    return 0;
}