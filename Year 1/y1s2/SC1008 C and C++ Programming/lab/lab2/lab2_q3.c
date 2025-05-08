#include <stdio.h>
int square1(int num);
void square2(int num, int *result);
int main()
{
    int number, result = 0;
    printf("Enter the number: \n");
    scanf("%d", &number);
    printf("square1(): %d\n", square1(number));
    square2(number, &result);
    printf("square2(): %d\n", result);
    return 0;
}
int square1(int num)
{
    int result = 0;
    int currentValue = 1;
    if (num > 0)
    {
        for (int i = 1; i < num; i++)
        {
            currentValue = currentValue + 2;
            result += currentValue;
            // printf("current value is %d\n", currentValue);
        }
        result += 1;
    }
    else
    {
        return 0;
    }

    return result;
    // printf("value outside is %d\n", result);
}
void square2(int num, int *result)
{
    int currentValue = 1;
    if (num > 0)
    {
        for (int i = 1; i < num; i++)
        {
            currentValue = currentValue + 2;
            *result += currentValue;
            // printf("current value is %d\n", currentValue);
        }
        *result += 1;
    }
    else
    {
        *result = 0;
    }
}