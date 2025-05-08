#include <stdio.h>
int rDigitPos1(int num, int digit);
void rDigitPos2(int num, int digit, int *pos);
int main()
{
    int number, digit, result = 0;
    printf("Enter the number: \n");
    scanf("%d", &number);
    printf("Enter the digit: \n");
    scanf("%d", &digit);
    printf("rDigitPos1(): %d\n", rDigitPos1(number, digit));
    rDigitPos2(number, digit, &result);
    printf("rDigitPos2(): %d\n", result);
    return 0;
}
int rDigitPos1(int num, int digit)
{
    /* Write your program code here */
    if (num == 0)
    {
        return 0;
    }
    else
    {
        if (num % 10 == digit)
        {
            return 1;
        }
        else
        {
            int pos = rDigitPos1(num / 10, digit);  
            return (pos == 0) ? 0 : pos + 1;
        }
    }
}
void rDigitPos2(int num, int digit, int *pos)
{
    /* Write your program code here */
    if (num == 0)
    {
        *pos = 0;
        return;
    }

    rDigitPos2(num / 10, digit, pos);
    *pos += 1;

    if (num % 10 == digit)
    {   // keep current pos
        return;
    }
    
}