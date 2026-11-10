#include <stdio.h>
int main(){
    int arr[] = {78, 45, 92, 63, 55, 81, 39};
    int n = sizeof(arr) / sizeof(arr[0]);
    int i, j, temp;
    for(i = 0; i < n-1; i++){
        for(j = 0; j < n-i-1; j++){
            if(arr[j] > arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    printf("Sorted List\n");
    for(i = 0; i < n; i++){
        printf("%d\n", arr[i]);
    }
    return 0;
}
