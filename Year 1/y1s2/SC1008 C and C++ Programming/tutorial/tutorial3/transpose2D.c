
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 10

// void transpose2D(int ar[][SIZE], int rowSize, int colSize);

void transpose2D(int ar[][SIZE], int rowSize, int colSize)
{
    for (int i = 0; i < rowSize; i++)
    {
        for (int j = i+1; j < colSize; j++)
        {
            int temp = ar[i][j];
            ar[i][j] = ar[j][i];
            ar[j][i] = temp;
        }
    }
}

void printArr(int ar[][SIZE], int rowSize, int colSize)
{
    for (int i = 0; i < rowSize; i++)
    {
        for (int j = 0; j < colSize; j++)
        {
            printf("%d ", ar[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    int rowSize = 4;
    int colSize = 4;

    int ar[SIZE][SIZE] = {{1, 2, 3, 4},
                          {5, 1, 2, 2},
                          {6, 3, 4, 4},
                          {7, 5, 6, 7}};
    printf("Before transpose: \n");
    printArr(ar, rowSize, colSize);

    printf("After transpose: \n");
    transpose2D(ar, rowSize, colSize);
    printArr(ar, rowSize, colSize);
    return 0;
}