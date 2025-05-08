#include <stdio.h>
#include <math.h>
int digitValue1(int num, int k);
void digitValue2(int num, int k, int *result);

int main()
{
    int num, digit, result = -1;

    printf("Enter the number: \n");
    scanf("%d", &num);
    printf("Enter k position: \n");
    scanf("%d", &digit);
    printf("digitValue1(): %d\n", digitValue1(num, digit));
    digitValue2(num, digit, &result);
    printf("digitValue2(): %d\n", result);
    return 0;
}
int digitValue1(int num, int k)
{
    int divisor = pow(10, k - 1);
    // printf("divisor: %d\n", divisor);
    // printf("num: %d\n", num);
    if (divisor > num)
    {
        return 0;
    }
    return (num / divisor) % 10;
}
void digitValue2(int num, int k, int *result)
{   

    int divisor = pow(10, k - 1);
    if( divisor > num){
        *result = 0;
    }else {
        *result = (num / divisor) % 10;
    }
}