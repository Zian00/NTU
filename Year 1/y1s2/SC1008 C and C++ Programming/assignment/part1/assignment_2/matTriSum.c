#include <stdio.h>
#define M 10
int matTriSum(int x[M][M], int n);
int main()
{
    int x[M][M];
    int n, i, j, s;

    printf("Enter array (nxn) size (n<=10): \n");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        printf("Enter row %d: \n", i);
        for (j = 0; j < n; j++)
            scanf("%d", &x[i][j]);
    }
    s = matTriSum(x, n);
    printf("The sum is: %d\n", s);
    return 0;
}
int matTriSum(int x[M][M], int n)
{   
    int sum =0;
    /* Write your code here */
    for(int j= 0; j < n; j ++){
        for(int i = 0; i <= j; i ++){
            // printf("here: %d\n", x[i][j]);
            sum += x[i][j];
        }
    }
    return sum;
}