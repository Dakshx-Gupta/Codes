// #include <stdio.h>
// void swapbycall(int a, int b){
//     int temp = a;
//     a = b;
//     b = temp;
// }
// int main(){
//     int x = 5;
//     int y = 6;
//     swapbycall(x, y);
//     printf("%d & %d", x , y);
//     return 0;
// }

void swapbyreference(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
int main(){
    int x = 5;
    int y = 6;
    swapbyreference(&x, &y);
    printf("After change: x = %d , y = %d", x, y);
    return 0;
}
