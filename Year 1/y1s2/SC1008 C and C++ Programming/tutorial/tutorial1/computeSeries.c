/*
Test Case 1:
Enter x:
0.9
Result = 2.46
*/
#include <stdio.h>
#include <math.h>

unsigned int factorial(unsigned int n)
{

    // Base Case:
    if (n == 1)
    {
        return 1;
    }

    // Multiplying the current N with the previous product of Ns
    return n * factorial(n - 1);
}
int main()
{
    /* Write your program code here */
    float x, etopowerx;
    printf("Enter x: ");
    scanf("%f", &x);
    printf("\n");

    for (int i = 1; i <= 10; i++)
    {
        etopowerx += pow(x, i) / factorial(i);
    };
    etopowerx += 1;
    printf("Result = %.2f\n", etopowerx);

    return 0;
}