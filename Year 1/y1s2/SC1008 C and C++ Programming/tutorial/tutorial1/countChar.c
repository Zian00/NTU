// . (countChars) Write a C program that reads in character by character from an input
// source, until ‘#’ is entered. The output of the program is the number of English letters
// and the number of digits that appear in the input.
// A sample program is given below:

// Test Case 1:
// Enter your characters (# to end):
// happy 34567 fans#
// The number of digits: 5
// The number of letters: 9

#include <stdio.h>
int main()
{
    /* Write your program code here */
    char ch;
    int countLetters = 0, countDigits = 0;
    printf("Enter your characters (# to end):\n");
    while ((ch = getchar()) != '#') {
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
            countLetters++;
        } else if (ch >= '0' && ch <= '9') {
            countDigits++;
        }
    }
    printf("The number of digits: %d\n", countDigits);
    printf("The number of letters: %d\n", countLetters);
    return 0;
}