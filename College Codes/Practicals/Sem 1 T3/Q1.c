// #include <stdio.h>
// int main(){
//     int row = 5;
//     for(int i = 1; i <=5; i++){
//         printf("\n");
//         for(int j = 1; j<i; j++){
//             printf(" *");
//         }
//     }
//     return 0;
// }


// #include <stdio.h>
// int main(){
//     int row = 5;
//     int i, j;
//     i = 1;
//     while(i <= row){
//         j = 1;
//         while(j <= i){
//             printf("*");
//             j++;
//         }
//         printf("\n");
//         i++;
//     }
//     return 0;
// }


int main(){
    int n = 5;
    int i, j;
    i = 1;
    do {
        j = 1;
        do {
            printf("*");
            j++;
        } while (j <= i);
        printf("\n");
        i++;
    } while (i <= n);
    
    return 0;
}
