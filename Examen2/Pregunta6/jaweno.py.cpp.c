# if 0
import sys
from math import log, floor

def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

def fib(n):
    f1 = 0
    f2 = 1
    while n:
        t = f2
        f2 = f1 + f2
        f1 = t
        n -= 1
    return f1, f2

n = int(sys.argv[1])
f1, f2 = fib(n)
jaweno = fact(f2)//(fact(f2-f1)*fact(f1))
print(int(floor(log(jaweno, 2))))
"""
# endif

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

int fib(int n){
    int f1 = 0, f2 = 1;
    while(n--) {
        int t = f2;
        f2 += f1;
        f1 = t;
    }
    return f1;
}

double logfact(int n) {
    if (n < 2) return log2(n);
    return log2(n) + logfact(n-1);
}

int main(int argc, char** argv) {

    int n = atoi(argv[1]);
    
    if (n == 0 || n == 1) printf("0\n");
    else { 
        int f1 = fib(n);
        int f2 = fib(n+1);
        double jaweno = logfact(f2) - logfact(f2-f1) - logfact(f1);
        printf("%.0lf\n",floor(jaweno));
    }
    return 0;
}

# if 0
"""
# endif