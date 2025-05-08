#include <stdio.h>
#include <string.h>
#define M1 "How are ya, sweetie?"

char M2[40] = "Beat the clock.";
char *M3 = "chat";
int main()
{
    char words[80], *p;
    printf(M1); // print out: How are ya, sweetie?
    puts(M1); // output: How are ya, sweetie?\n
    puts(M2); // output: Beat the clock.\n
    puts(M2 + 1); // output: eat the clock.\n
    fgets(words, 80, stdin); /* user inputs : win a toy. */
    if (p = strchr(words, '\n'))
        *p = '\0'; 
    puts(words); // output: win a toy.\n 
    scanf("%s", words + 6); /* user inputs : snoopy. */
    puts(words); // output: win a snoopy.
    words[3] = '\0';
    puts(words); // null terminated at index 3, output : win
    while (*M3)
        puts(M3++); // output: chat\0hat\0at\0t\0
        // pointer moves to \0 after exiting the loop
    puts(--M3); // output : t\0
    puts(--M3); // output: at\0
    M3 = M1;
    puts(M3); // output: How are ya, sweetie?\0
    return 0;
}