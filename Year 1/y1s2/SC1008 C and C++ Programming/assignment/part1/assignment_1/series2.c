#include <stdio.h>
int main()
{
    /* Write your code here */
    int denominator = 1;
    double x, result = 1, numerator = 1;
    printf("Enter a number:\n");
    scanf("%lf", &x);
    for (int i = 1; i <= 20; i++)
    {
        denominator *= i;
        numerator *= x;
        // printf("denominator is %d, numerator is %.2f, result is %.2f\n", denominator, numerator, result);
        if (i % 2 == 0)
        {
            result += numerator / (float)denominator;
        }
        else
        {
            result -= numerator / (float)denominator;
        }
    }
    printf("Result = %.2f\n", result);

    return 0;
}