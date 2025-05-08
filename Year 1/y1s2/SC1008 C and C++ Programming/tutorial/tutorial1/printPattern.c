/*
(printPattern) Write a C program that reads a positive number height between 1 and 9
as its input value, and prints a triangular pattern according to height. Note that only 1, 2
and 3 are used to generate the patterns. For example, when height = 3, it will print the
following pattern:
1
22
333
while height = 7 will print the following pattern:
1
22
333
1111
22222
333333
1111111


Test Case 2:
Enter the height:
7
Pattern:
1
22
333
1111
22222
333333
1111111
*/

#include <stdio.h>
int main()
{
    /* Write your program code here */
    int height;
    printf("height (between 1 and 9): ");
    scanf("%d", &height);

    while (height > 9 && height < 1)
    {
        printf("Invalid height\n");
        printf("height (between 1 and 9): ");
        scanf("%d", &height);
    }
    printf("Pattern:\n");
    for (int i = 1; i <= height; i++)
    {
        int num = (i -1) % 3 +1;
        for (int j = 0; j < i; j++){
            printf("%d", num);
        }
        
        printf("\n");
    }

    return 0;
}
