#include <stdio.h>
#include <string.h>
char *stringncpy(char *s1, char *s2, int n);
int main()
{
    char targetStr[40], sourceStr[40], *target, *p;
    int length;

    printf("Enter the string: \n");
    fgets(sourceStr, 40, stdin);
    if (p = strchr(sourceStr, '\n'))
        *p = '\0';
    printf("Enter the number of characters: \n");
    scanf("%d", &length);
    target = stringncpy(targetStr, sourceStr, length);
    printf("stringncpy(): %s\n", target);
    return 0;
}
char *stringncpy(char *s1, char *s2, int n)
{
    /* Write your code here */
    int i;
    for ( i = 0; i < n && s2[i] != '\0'; i++)
    {
        s1[i] = s2[i];
    }
    for (; i < n; i++){
        s1[i] = '\0';
    }

    return s1;
}