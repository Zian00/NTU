#include <stdio.h>
#define N 20
int main()
{
    int a[N], i, j, k, m;
    int size;
    /* Write your code here – for additional local variables */
    int b[N];
    printf("Enter array size: \n");
    scanf("%d", &size);
    printf("Enter %d data: \n", size);
    for (i = 0; i < size; i++)
        scanf("%d", &a[i]);
    printf("Result: \n");
    /* Write your code here */
    for (int i = 0; i < size; i++)
    {
        // store the last element
        int temp = a[size - 1];

        // shift back by one index
        for (int j = 0; j < size - 1; j++)
        {

            b[j + 1] = a[j];
        }
        // put the last element to first index
        b[0] = temp;
        // load the shifted array back to array a
        for (int m = 0; m < size; m++)
        {
            a[m] = b[m];
        }
        for (int k = 0; k < size; k++)
        {
            printf("%d", a[k]);
        }
        printf("\n");
    }
    return 0;
}