/*
Write a function that extracts the odd digits from a positive number, and
combines the odd digits sequentially into a new number. The new number is returned to the
calling function. If the input number does not contain any odd digits, then the function returns -
1. For example, if the input number is 1234567, then 1357 will be returned; and if the input
number is 24, then –1 will returned.
*/
#include <stdio.h>
#define INIT_VALUE 999
int extOddDigits1(int num);
void extOddDigits2(int num, int *result);
int main()
{
    int number, result = INIT_VALUE;

    printf("Enter a number: \n");
    scanf("%d", &number);
    printf("extOddDigits1(): %d\n", extOddDigits1(number));
    extOddDigits2(number, &result);
    printf("extOddDigits2(): %d\n", result);
    return 0;
}
int extOddDigits1(int num)
{
    int digitLeft;
    int newValue = 0;
    int i = 1;

    // 12345
    // 1234
    // 123
    while (num > 0)
    {
        digitLeft = (int)num % 10; // get the last digit
        // printf("digitLeft: %d\n", digitLeft);
        if (digitLeft % 2 != 0)
        {
            newValue += digitLeft * i;
            // printf("newValue: %d\n", newValue);
            i *= 10;
        }
        num /= 10;
    }
    return newValue == 0 ? -1 : newValue;
}
void extOddDigits2(int num, int *result)
{
    int digitLeft;
    *result = 0;
    int i = 1;

    while (num > 0)
    {
        digitLeft = (int)num % 10; // get the last digit
        // printf("digitLeft: %d\n", digitLeft);
        if (digitLeft % 2 != 0)
        {
            *result += digitLeft * i;
            // printf("newValue: %d\n", newValue);
            i *= 10;
        }
        num /= 10;
    }
    *result =  *result == 0 ? -1 : *result;
    
}
