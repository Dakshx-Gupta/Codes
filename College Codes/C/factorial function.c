#include <stdio.h>
int factorial(int n){
    int fact = 1;
    for(int i = 1; i <= n; i++){
        fact = fact * i;
    }
    return fact;
}

int main(){
    int num = 5;
    printf("Factorial is: %d", factorial(num));
    return 0;
    
}
