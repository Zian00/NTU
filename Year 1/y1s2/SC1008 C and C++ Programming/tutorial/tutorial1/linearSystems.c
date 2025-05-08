#include <stdio.h>
#include <math.h>
int main()
{
    /* Write your program code here */

    //  The program reads in a1, b1, c1, a2, b2 and c2, and then computes and prints the solutions.
    // In your program, if the denominator (a1b2 - a2b1) of the above equations is zero, then it
    // prints an error message “Unable to compute because the denominator is zero!”.
    float a1, b1, c1, a2, b2, c2, x, y, floating_denorminator;
    printf("Enter the values for a1, b1, c1, a2, b2, c2:\n");
    scanf("%f %f %f %f %f %f", &a1, &b1, &c1, &a2, &b2, &c2);
    floating_denorminator = a1 * b2 - a2 * b1;
    if (floating_denorminator == 0)
    {
        printf("Unable to compute because the denominator is zero!\n");
    }
    else
    {
        x = (b2 * c1 - b1 * c2) / floating_denorminator;
        y = (a1 * c2 - a2 * c1) / floating_denorminator;
        printf("x = %.2f and y = %.2f\n", x, y);
    }

    return 0;
}

// Test Case 1:
// Enter the values for a1, b1, c1, a2, b2, c2:
// 1 1 1 5 7 9
// x = -1.00 and y = 2.00