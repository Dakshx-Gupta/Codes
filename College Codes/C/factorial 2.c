#include <stdio.h>
int main(){
    int r = 1;
    int n = 5;
    if(n == 0){
        printf("Factorial of 0 is 0");
    }
    else{
        for(int i = 1; i <=n; i++){
            r = r * i;
        }
    printf("%d", r);
    }
    return 0 ;
}
