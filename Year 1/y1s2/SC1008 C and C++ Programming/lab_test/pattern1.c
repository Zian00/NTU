#include <stdio.h>
int main()
{
    /* Write your code here */
    int userInput;
    printf("Enter the height: \n");
    scanf("%d", &userInput);
    
    for( int i =1; i <=userInput; i ++){
        for(int j =1; j <=userInput -i; j++){
            printf(" ");
        }
        for(int j =1; j <=(i+i-1); j++){
            printf("*");
        }
        for(int j =1; j <=userInput -i; j++){
            printf(" ");
        }
        printf("\n");
    }




    return 0;
}