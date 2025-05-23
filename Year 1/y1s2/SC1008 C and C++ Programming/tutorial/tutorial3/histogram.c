/*
(histogram) Write a program which will draw the histogram for n integers from 0 to 99.
N is input by the user. Each of the n numbers will be generated by calling rand() % 100.
The program will consist of two functions (i) to collect the frequency distribution of the
numbers (ii) to print the histogram. An example histogram is shown here.
0 – 9 |*********************
10 – 19 |************
20 – 29 |*************
30 – 39 |**
…......
90 – 99 |***************
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// int collectFreq(int freq[], int userInput);
// void printHistogram(int freq[]);

int collectFreq(int freq[], int userInput)
{

    for (int i = 0; i < userInput; i++)
    {
        int num = rand() % 100;
        int bin = num/10;
        freq[bin]++;
        // printf("freq[%d] = %d\n", num / 10, freq[num / 10]);
    }
}

void printHistogram(int freq[])
{
    for (int i = 0; i < 10; i++)
    {
        printf("%2d - %2d | ", i*10, (1+i)* 10 -1);
        // printf("freq[i] : %d\n", freq[i]);
        for(int j =0; j < freq[i]; j++){
            printf("*");
        }
        printf("\n");
    }
}

int main()
{
    int userInput;
    int freq[10] = {0};
    srand(time(NULL));
    printf("Please enter a value from 0 to 99: ");
    scanf("%d", &userInput);
    collectFreq(freq, userInput);
    printHistogram(freq);

    return 0;
}
