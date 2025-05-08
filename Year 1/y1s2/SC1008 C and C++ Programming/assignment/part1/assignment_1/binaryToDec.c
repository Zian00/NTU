#include <stdio.h>
#include <math.h>
int main()
{
    /* Write your code here */
    long long int binaryInput;
    int decValue = 0;
    int powPlace = 0;
    printf("Enter a binary number:\n");
    scanf("%lld", &binaryInput);
    while (binaryInput > 0)
    {
        if (binaryInput % 10 == 1)
        {
            // decValue += pow(2, powPlace);
            decValue += (1 << powPlace);
        }

        binaryInput /= 10;
        powPlace += 1;
    }
    printf("The equivalent decimal number: %d", decValue);
    return 0;
}