#include <stdio.h>
int main()
{
    int yearInput, resultYear;
    /* Write your code here */
    while (1)
    {
        printf("Enter your birth year:\n");
        scanf("%d", &yearInput);
        if (yearInput == -1)
        {
            break;
        }
        resultYear = (yearInput - 4) % 12;
        // printf("resultYear is %d\n", resultYear);
        switch (resultYear)
        {
        case 0:
            printf("chineseHoroscope: Rat\n");
            break;
        case 1:
            printf("chineseHoroscope: Cow\n");
            break;
        case 2:
            printf("chineseHoroscope: Tiger\n");
            break;
        case 3:
            printf("chineseHoroscope: Rabbit\n");
            break;
        case 4:
            printf("chineseHoroscope: Dragon\n");
            break;
        case 5:
            printf("chineseHoroscope: Snake\n");
            break;
        case 6:
            printf("chineseHoroscope: Horse\n");
            break;
        case 7:
            printf("chineseHoroscope: Goat\n");
            break;
        case 8:
            printf("chineseHoroscope: Monkey\n");
            break;
        case 9:
            printf("chineseHoroscope: Rooster\n");
            break;
        case 10:
            printf("chineseHoroscope: Dog\n");
            break;
        case 11:
            printf("chineseHoroscope: Pig\n");
            break;
        }
    }

    return 0;
}
