#include <stdio.h>
int main()
{
    /* Write your code here */
    double listPrice, carPrice;
    int cat;

    printf("Please enter the list price:\n");
    scanf("%lf", &listPrice);
    printf("Please enter the category:\n");
    scanf("%d", &cat);

    if (cat < 1 || cat > 4)
    {
        printf("Invalid category. Please enter a value between 1 and 4.\n");
        return 1;
    }
    carPrice = listPrice * 0.9 * 1.03;
    if (carPrice > 100000)
    {
        carPrice *= 1.1;
    }

    double additionalPrices[] = {70000, 80000, 23000, 600};
    printf("Total price is $%.2f\n", additionalPrices[cat - 1] + carPrice);

    return 0;
}