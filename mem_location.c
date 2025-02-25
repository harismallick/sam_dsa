#include <stdio.h>

int main() {
    int a = 10;
    int *p = &a;
    printf("Address of a: %p\n", &a);
    printf("Value of p: %p\n", p);
    printf("Value of a: %d\n", a);
    printf("Value of *p: %d\n", *p);
    a = 12;
    printf("Value of *p: %d\n", *p);
    int **g = &p;
    int ***h = &g;
    printf("Value stored in a using pointer g: %d\n", **g);
    printf("Memory address of p is %p\n", &p);
    printf("Value stored in pointer g: %p\n", *g);
    int p = 12;
    return 0;
}