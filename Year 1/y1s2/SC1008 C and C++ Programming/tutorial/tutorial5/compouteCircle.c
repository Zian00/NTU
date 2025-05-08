#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define INIT_VALUE -1000
struct circle
{
    double radius;
    double x;
    double y;
};
int intersect(struct circle, struct circle);
int contain(struct circle *, struct circle *);
int main()
{
    struct circle c1, c2;
    int choice, result = INIT_VALUE;

    printf("Select one of the following options: \n");
    printf("1: intersect()\n");
    printf("2: contain()\n");
    printf("3: exit()\n");
    do
    {
        result = -1;
        printf("Enter your choice: \n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter circle 1 (radius x y): \n");
            scanf("%lf %lf %lf", &c1.radius, &c1.x, &c1.y);
            printf("Enter circle 2 (radius x y): \n");
            scanf("%lf %lf %lf", &c2.radius, &c2.x, &c2.y);
            result = intersect(c1, c2);
            if (result == 1)
                printf("intersect(): intersect\n");
            else if (result == 0)
                printf("intersect(): not intersect\n");
            else
                printf("intersect(): error\n");
            break;
        case 2:
            printf("Enter circle 1 (radius x y): \n");
            scanf("%lf %lf %lf", &c1.radius, &c1.x, &c1.y);
            printf("Enter circle 2 (radius x y): \n");
            scanf("%lf %lf %lf", &c2.radius, &c2.x, &c2.y);
            result = contain(&c1, &c2);
            if (result == 1)
                printf("contain(): contain\n");
            else if (result == 0)
                printf("contain(): not contain\n");
            else
                printf("contain(): error\n");
            break;
        }
    } while (choice < 3);
    return 0;
}
int intersect(struct circle c1, struct circle c2)
{
    /* Write your code here */

    double cond = sqrt(pow((c2.x - c1.x), 2) + pow((c2.y - c1.y), 2));
    if (cond <= (c1.radius + c2.radius))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int contain(struct circle *c1, struct circle *c2)
{
    /* Write your code here */
    /*
    Implement the function contain() that returns 1 if c1 contains c2, i.e. circle c2 is found
    inside circle c1. Otherwise, the function returns 0.
    Circle c1 contains circle c2 when the radius of c1 is larger than or equal to the sum of the radius of c2 and the distance
    between the centres of c1 and c2
    */
    double c1Cc2 = c1->radius;
    double cond = (c2->radius + sqrt(pow((c2->x - c1->x), 2) + pow((c2->y - c1->y), 2)));
    if (c1Cc2 >= cond)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}