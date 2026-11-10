#include <stdio.h>
int main()
{
    for(int i = 1; i<10; i++){
        if(i == 4){
            printf("Done\n");
            break;
        }
        else{
            printf("Number: %d\n", i);
        }

    }
    return 0;
}
