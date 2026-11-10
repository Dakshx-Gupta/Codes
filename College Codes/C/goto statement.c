#include <stdio.h>
int main()
{
    int a = 4;
    int b = 2;

    if (a % b == 0){
        goto even;
    }
    else{
        goto odd;
    }

    even:
    printf("Number is even");
    return 0;

    odd:
    printf("number is odd");
    return 0;
}
