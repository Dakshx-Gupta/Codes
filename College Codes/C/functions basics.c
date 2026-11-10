#include <stdio.h>
int add(int a, int b){
    return a + b;
}
int main(){
    int i = 2, j = 2;
    int sum = add(i, j);
    printf("%d", sum);
    return 0; 
}
