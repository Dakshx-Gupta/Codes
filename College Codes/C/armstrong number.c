#include <stdio.h>
int main()
{
    int n, temp, sum = 0, digit;
    printf("Enter any positive integer: ");
    scanf("%d", &n);
    temp = n;

    while(temp != 0){
        digit = temp % 10;
        sum = sum + digit*digit*digit;
        temp = temp / 10;
    }
    if(sum == n){
        printf("Number is armstrong");
    }
    else{
        printf("Not armstrong");
    }
    return 0;
}
