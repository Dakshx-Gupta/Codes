#include <stdio.h>
int main()
{
    int arr[10], n, key, i;
    int low, mid, high, found = 0;
    printf("Enter number of elements ");
    scanf("%d", &n);
    printf("Enter %d element\n", n);
    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    printf("Enter target element ");
    scanf("%d", &key);
    low = 0;
    high = n-1;
    while(low <= high){
        mid = (low + high ) / 2;
        if(arr[mid] == key){
            printf("Element %d found at position %d (index %d)\n", key, 
            mid + 1, mid);
            found = 1;
            break;
        }
        else if (arr[mid] < key){
            low = mid + 1;
        }
        else{
            high = mid - 1;
        }
    }
    if (!found){
        printf("Element %d not found in the list \n", key);   
    }
    return 0;
}
