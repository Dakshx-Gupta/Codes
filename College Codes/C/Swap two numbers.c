#include <stdio.h>
int main(){
int a, b, c;

printf("Enter two numbers: ");
scanf("%d %d", &a, &b);
a= a+b;
b= a-b;
a= a-b;

printf("%d + %d = %d\n", a, b, c);
return 0;
}
