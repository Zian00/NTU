#include <stdio.h>
#include <string.h>
struct student
{
    char name[20];    /* student name */
    double testScore; /* test score */
    double examScore; /* exam score */
    double total;     /* total = (testScore+examScore)/2 */
};
double average();
int main()
{
    printf("average(): %.2f\n", average());
    return 0;
}
double average()
{
    /* Write your code here */
    struct student students[50];
    char name[50];
    int count = 0;
    double sum = 0;
    while (1)
    {
        printf("Enter student name:\n");
        scanf("%s", students[count].name);
        if (strcmp( students[count].name, "END") == 0)
        {
            break;
        }
        printf("Enter test score:\n");
        scanf("%lf", &students[count].testScore);
        printf("Enter exam score:\n");
        scanf("%lf", &students[count].examScore);
        students[count].total = (students[count].examScore + students[count].testScore) / 2;
        printf("Student %s total= %.2lf\n", students[count].name, students[count].total);
        sum += students[count].total;
        count++;
    }
    if (count == 0)
    {
        return 0;
    }
    return sum / count;
}