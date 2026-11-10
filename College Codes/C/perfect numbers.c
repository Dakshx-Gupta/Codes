#include <stdio.h>
int main()
{
    int n, i, sum = 0; 
    printf("Enter the number to check: ");
    scanf("%d", &n);
    for(i = 1; i < n; i++)
    {
        if (n % i == 0)
        sum = sum + i;
    }
    if (n == sum){
        printf("number is perfect");
    }
    else{
        printf("not perfect");
    }

    return 0;
}
