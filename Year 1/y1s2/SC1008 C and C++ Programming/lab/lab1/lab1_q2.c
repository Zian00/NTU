#include <stdio.h>
int main()
{
    /* Write your code here */
    int numOfLine;
    printf("Enter number of lines:\n");
    scanf("%d", &numOfLine);
    for (int i = 0; i < numOfLine; i++)
    {
        printf("Enter line %d (end with -1):\n", i + 1);
        float avg = 0;
        int sum = 0;
        int count = 0;
        int num;
        while (1)
        {
            scanf("%d", &num);
            if (num == -1)
            {
                break;
            }
            sum += num;
            count++;
        }
        avg = (float)sum / count;
        printf("Average = %.2f\n", avg);
        
    }
    return 0;
}