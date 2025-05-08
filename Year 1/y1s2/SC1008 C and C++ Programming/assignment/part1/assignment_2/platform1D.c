#include <stdio.h>
int platform1D(int ar[], int size);
int main()
{
    int i, b[50], size;
    printf("Enter array size: \n");
    scanf("%d", &size);
    printf("Enter %d data: \n", size);
    for (i = 0; i < size; i++)
        scanf("%d", &b[i]);
    printf("platform1D(): %d\n", platform1D(b, size));
    return 0;
}
int platform1D(int ar[], int size)
{
    /* Write your code here */
    int count = 1;
    int maxcount = 1;
    for (int i = 0; i < size - 1; i++)
    {
        if (ar[i] == ar[i + 1])
        {   
            // printf("ar[i]: %d\n",ar[i]);
            // printf("ar[i+1]: %d\n", ar[i+1]);
            count += 1;
        }
        else {
            count = 1;
        }
        if (count > maxcount)
        {
            maxcount = count;
        }
    }

    return maxcount;
}