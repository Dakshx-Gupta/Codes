#include <stdio.h>
void swap(int *xp , int *yp){
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
void selectionsort(int arr[], int n){
    int i, j, min;
    for(i = 0; i < n-1; i++){
        min = i;
        for(j = i+1; j < n; j++){
            if(arr[j] < arr[min]){
                min = j;
            }
        }
        if(min != i){
            swap(&arr[min], &arr[i]);
        }
    }   
}
void print(int arr[], int size){
    for(int i = 0; i < size; i++){
        printf("%d", arr[i]);
    }
}
int main(){
    int arr[100], n, i;
    printf("Enter no. of elements: ");
    scanf("%d", &n);
    printf("Enter %d integers: ", n);
    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    printf("\n Original Array\n");
    print(arr, n);
    selectionsort(arr, n);
    printf("\nSorted Array\n");
    print(arr, n);
    return 0;
}
