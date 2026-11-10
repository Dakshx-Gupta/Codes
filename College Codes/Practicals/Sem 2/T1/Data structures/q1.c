#include <stdio.h>
int main()
{
    int arr[] = {2, 5, 9, 14, 18, 21, 27, 30, 35};
    int key = 21;
    int i;
    int n = sizeof(arr) / sizeof(arr[0]);
    int low, mid, high, found = 0;
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
