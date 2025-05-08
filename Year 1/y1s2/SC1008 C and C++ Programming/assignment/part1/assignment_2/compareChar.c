#include <stdio.h>
#include <string.h>
void compareChar(char *str1, char *str2, char *str3);
int main()
{
    char str1[80], str2[80], str3[80];

    printf("Enter the first string: \n");
    scanf("%s", str1);
    printf("Enter the second string: \n");
    scanf("%s", str2);
    compareChar(str1, str2, str3);
    printf("compareChar(): %s\n", str3);
    return 0;
}
void compareChar(char *str1, char *str2, char *str3)
{
    /* Write your code here */
    int i = 0;
    int max_len_string = (strlen(str1) >= strlen(str2)) ? strlen(str1) : strlen(str2);

    for (i = 0; i < max_len_string; i++)
    {
        if (i < strlen(str1) && i < strlen(str2))
        {
            if (str1[i] == str2[i])
            {
                str3[i] = str1[i];
            }
            else if (str1[i] > str2[i])
            {
                str3[i] = str1[i];
            }
            else if (str2[i] > str1[i])
            {
                str3[i] = str2[i];
            }
        }
        else if (i < strlen(str1))
        {
            str3[i] = str1[i];
        }
        else
        {
            str3[i] = str2[i];
        }
    }
    str3[i] = '\0';
}