#include <stdio.h>
#include <string.h>
#define MAX 100
typedef struct
{
    char name[20];
    int telno;
} PhoneBk;
void printPB(PhoneBk *pb, int size);
int readin(PhoneBk *pb);
void search(PhoneBk *pb, int size, char *target);
int main()
{
    PhoneBk s[MAX];
    char t[20], *p;
    int size = 0, choice;
    char dummychar;

    printf("Select one of the following options: \n");
    printf("1: readin()\n");
    printf("2: search()\n");
    printf("3: printPB()\n");
    printf("4: exit()\n");
    do
    {
        printf("Enter your choice: \n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            scanf("%c", &dummychar);
            size = readin(s);
            break;
        case 2:
            scanf("%c", &dummychar);
            printf("Enter search name: \n");
            fgets(t, 20, stdin);
            if (p = strchr(t, '\n'))
                *p = '\0';
            search(s, size, t);
            break;
        case 3:
            printPB(s, size);
            break;
        }
    } while (choice < 4);
    return 0;
}
void printPB(PhoneBk *pb, int size)
{
    /* Write your code here */
    printf("The phonebook list:\n");
    for (int i = 0; i < size; i++)
    {
        printf("Name: %s\n", pb[i].name);
        printf("Telno: %d\n", pb[i].telno);
    }
}
int readin(PhoneBk *pb)
{
    /* Write your code here */
    int size = 0;
    while (1)
    {
        printf("Enter name:\n");
        scanf("%s", pb[size].name);
        if (strcmp(pb[size].name, "#") == 0)
        {
            break;
        }
        printf("Enter Tel:\n");
        scanf("%d", &pb[size].telno);
        // pb++;
        size++;
    }
    return size;
}
void search(PhoneBk *pb, int size, char *target)
{
    /* Write your code here */
    for (int i = 0; i < size; i++)
    {
        if (strcmp(pb[i].name, target) == 0)
        {
            printf("Name: %s\n", pb[i].name);
            printf("Tel: %d\n", pb[i].telno);
            return;
        }
    }
    printf("Name not found!\n");
}