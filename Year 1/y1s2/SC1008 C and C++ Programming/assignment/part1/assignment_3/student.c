#include <stdio.h>
#include <string.h>
#define SIZE 50
typedef struct
{
    int id;
    char name[50];
} Student;
void inputStud(Student *s, int size);
void printStud(Student *s, int size);
int removeStud(Student *s, int *size, char *target);
int main()
{
    Student s[SIZE];
    int size = 0, choice;
    char target[80], *p;
    int result;
    char dummy[80];

    printf("Select one of the following options: \n");
    printf("1: inputStud()\n");
    printf("2: removeStud()\n");
    printf("3: printStud()\n");
    printf("4: exit()\n");
    do
    {
        printf("Enter your choice: \n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter size: \n");
            scanf("%d", &size);
            printf("Enter %d students: \n", size);
            inputStud(s, size);
            break;
        case 2:
            printf("Enter name to be removed: \n");
            fgets(dummy, 80, stdin);
            fgets(target, 80, stdin);
            if (p = strchr(target, '\n'))
                *p = '\0';
            printf("removeStud(): ");
            result = removeStud(s, &size, target);
            if (result == 0)
                printf("Successfully removed\n");
            else if (result == 1)
                printf("Array is empty\n");
            else if (result == 2)
                printf("The target does not exist\n");
            else
                printf("An error has occurred\n");
            break;
        case 3:
            printStud(s, size);
            break;
        }
    } while (choice < 4);
    return 0;
}
void inputStud(Student *s, int size)
{
    /* Write your code here */
    char dummy[50];
    char *p;
    for (int i = 0; i < size; i++)
    {
        printf("Student ID:\n");
        scanf("%d", &s[i].id);
        // getchar();
        fgets(dummy, 80, stdin);
        printf("Student Name:\n");

        fgets(s[i].name, 50, stdin);
        if ( p = strchr(s[i].name, '\n'))
            *p = '\0';

        // scanf(" %49[^\n]", s[i].name);
    }
}
void printStud(Student *s, int size)
{
    int i;

    printf("The current student list: \n");
    if (size == 0)
        printf("Empty array\n");
    else
    {
        for (i = 0; i < size; i++)
        {
            printf("Student ID: %d ", s[i].id);
            printf("Student Name: %s\n", s[i].name);
        }
    }
}
int removeStud(Student *s, int *size, char *target)
{
    /* Write your code here */
    if (*size == 0)
    {
        return 1;
    }
    for (int i = 0; i < *size; i++)
    {
        if (strcmp(s[i].name, target) == 0)
        {
            // once found, need to loop again to shift behind forward
            for (int j = i; j < *size; j++)
            {
                s[j] = s[j + 1];
            }
            // last index is duplicated, but size -1 removes it from array
            *size -= 1;
            return 0;
        }
    }
    return 2;
}