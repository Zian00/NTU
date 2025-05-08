
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 10

void reduceMatrix2D(int ar[][SIZE], int rowSize, int colSize)
{
    for (int j = 0; j < colSize; j++)
    {
        for (int i = j + 1; i < rowSize; i++)
        {
            // [0][0], [1][1], [2][2], [3][3]
            // [1][0],
            // [2][0], [2][1],
            // [3][0], [3][1], [3][2]
            ar[j][j] += ar[i][j];
            // printf("ar[%d][%d] = %d\n", j, j, ar[j][j]);
            ar[i][j] = 0;
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

    int ar[SIZE][SIZE] = {{4, 3, 8, 6},
                          {9, 0, 6, 5},
                          {5, 1, 2, 4},
                          {9, 8, 3, 7}};
    printf("Before reduction: \n");
    printArr(ar, rowSize, colSize);

    printf("After reduction: \n");
    reduceMatrix2D(ar, rowSize, colSize);
    printArr(ar, rowSize, colSize);
    return 0;
}