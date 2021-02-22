#include <stdio.h>
#include "definitions.h"

// Recursive function. Literal translation
int f1 (int n) {
    int acum, i;
    
    if (n < ALPHA*BETA){
        return n;
    }
    for(i = 1, acum = 0; i <= ALPHA; i++) {
        acum += f1(n - BETA * i);
    }
    return acum;
}

// Tail recursion
int f2_aux (int x0, int x1, int x2, int x3, int x4, int x5, int x6, int n) {
    
    if (n < BETA) {
        return x0;
    }

    int x7 = x0+x1+x2+x3+x4+x5+x6;
    return f2_aux(x1,x2,x3,x4,x5,x6,x7,n-BETA);
}

// Auxiliar to set parameters
int f2 (int n) {
    int x = n % BETA;
    return f2_aux(x, 
                  x + BETA, 
                  x + 2*BETA, 
                  x + 3*BETA, 
                  x + 4*BETA, 
                  x + 5*BETA, 
                  x + 6*BETA, 
                  n);
}

// Iterative
int f3 (int n) {

    int x = n % BETA;
    int x0 = x;
    int x1 = x + BETA;
    int x2 = x + 2*BETA;
    int x3 = x + 3*BETA;
    int x4 = x + 4*BETA;
    int x5 = x + 5*BETA;
    int x6 = x + 6*BETA;
    while (n >= BETA) {
        int temp = x0+x1+x2+x3+x4+x5+x6;
        x0 = x1;
        x1 = x2;
        x2 = x3;
        x3 = x4;
        x4 = x5;
        x5 = x6;
        x6 = temp;
        n -= BETA;
    }
    return x0;
}

// Test
int main(int argc, char **argv) {
    
    if (argc != 2) {
        printf("Uso: ./test <funcion>\n<function>:\n");
        printf("1 -> Recursiva\n2 -> Recursiva de Cola\n3 -> Iterativa\n");
        return 1;
    }

    int n = argv[1][0] - '0';

    switch (n) {
        case 1:
            // recursive
            for(int i = 0; i < CASES; i++)
                printf("%d\n",f1(i));
            break;
        case 2:
            // recursive
            for(int i = 0; i < CASES; i++)
                printf("%d\n",f2(i));
            break;
        case 3:
            // recursive
            for(int i = 0; i < CASES; i++)
                printf("%d\n",f3(i));
            break;
    }
        
}  