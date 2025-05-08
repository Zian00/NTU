/*
int number;
int *p;

(i) p = 100; number = 8
a). number = 8
b). &number = 7700
c). p = 100
d). &p = 3478
e). *p = undefined , actly is the content of the memory location 100.

(ii)  number = p
a). number = 100
b). &number = 7700
c). p = 100
d). &p = 3478
e). *p = the content of the memory location 100.

(iii) p = &number
a). number = 100
b). &number = 7700
c). p = 7700 // p is pointing to the address of number
d). &p = 3478
e). *p = 100 // valued stored at address 7700

(iv) *p = 10 // modify value at address 7700 to 10
a). number = 10
b). &number = 7700
c). p = 7700 // p is poining to the address of number
d). &p = 3478
e). *p = 10 

(v) number = &p // number stores the address of p
a). number = 3478 // number changed to 3478
b). &number = 7700 // address of number
c). p = 7700
d). &p = 3478
e). *p = 3478

(vi) p = &p // address of p is stored in p
a). number = 3478
b). &number = 7700 
c). p = 3478 // p store the new value, which is  address of p
d). &p = 3478
e). *p = 3478 

*/