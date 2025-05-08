#include <stdio.h>
int main()
{
    int denominator = 1;
    float x, result = 1, numerator = 1;
    printf("Enter X:\n");
    scanf("%f", &x);
    for (int i = 1; i <= 10; i++)
    {
        denominator *= i;
        numerator *= x;
        printf("denominator is %d, numerator is %.2f, result is %.2f\n", denominator, numerator, result);
        result += numerator / (float)denominator;
    }
    printf("Result = %.2f\n", result);
    return 0;
}

/*
x= 10
1
10
result = (1) + 10/1

2
100
result = (1+ 10/1) + 100/2

6
1000
result = (1+ 10/1 + 100/2) + 1000/6

24
10000
result = (1+ 10/1 + 100/2 + 1000/6) + 10000/24
*/