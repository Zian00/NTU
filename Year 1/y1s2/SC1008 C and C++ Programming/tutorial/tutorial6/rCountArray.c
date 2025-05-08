#include <stdio.h>
#define SIZE 20
int rCountArray(int array[], int n, int a);
int main()
{
    int array[SIZE];
    int index, count, target, size;

    printf("Enter array size: \n");
    scanf("%d", &size);
    printf("Enter %d numbers: \n", size);
    for (index = 0; index < size; index++)
        scanf("%d", &array[index]);
    printf("Enter the target number: \n");
    scanf("%d", &target);
    count = rCountArray(array, size, target);
    printf("rCountArray(): %d\n", count);
    return 0;
}
int rCountArray(int array[], int n, int a)
{
    /* Write your program code here */

    if (n == 1)
    {
        if (array[0] == a)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        int count = (array[0] == a) ? 1 : 0;
        return count + rCountArray(array + 1, n - 1, a);
    }
}
