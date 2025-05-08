#include <stdio.h>
void add1(int ar[], int size);
int main()
{
    int array[3][4];
    int h, k;
    for (h = 0; h < 3; h++)
        for (k = 0; k < 4; k++)
            scanf("%d", &array[h][k]);
    for (h = 0; h < 3; h++)      /* line a */
        add1(array[h], 4);
    for (h = 0; h < 3; h++)
    {
        for (k = 0; k < 4; k++)
            printf("% 10d", array[h][k]);
        printf("\n");
    }
    return 0;
}
void add1(int ar[], int size)
{
    int k;
    for (k = 0; k < size; k++)
        ar[k]++;
}
/*
Explain how the addition of 1 to every element of the two dimensional array ‘array’ is
done in the following program

when add1 function is called, rows of array are passed into add1 function, each column of the rows is then added 1
inside the function. Addition is conducted row by row.

What if the for statement at ‘line a’ is replaced by this
statement:
add1(array[0], 3 * 4);

array[0] is the pointer to the first row of the 2D array, effectively pointing to the start of entire array.
The 2D array is flattened into 1D array of size 12 and additon is conducted in one row only.
*/