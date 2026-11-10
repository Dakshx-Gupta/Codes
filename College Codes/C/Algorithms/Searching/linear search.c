#include <stdio.h>
int main(){
    int arr[10], n, key, i, found = 0;
    printf("Enter number of elements ");
    scanf("%d", &n);
    printf("Enter %d element\n", n);
    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);
        
    }
    printf("Enter element to search ");
    scanf("%d", &key);
    for(i = 0; i < n; i++){
        if(arr[i] == key){
            printf("Element %d found at position %d (Index value %d)\n", key, i,
            i++);
            found = 1;
            break;
        }
    }
    if(! found){
        printf("Element %d not found in the list \n", key);
    }
    return 0;
}
