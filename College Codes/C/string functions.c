#include <stdio.h>
#include <string.h>
int main(){
    char a[50];
    int d;
    printf("Enter string:");
    // scanf("%s", &a);
    fgets(a, sizeof(a), stdin);
    // printf("%s", a);
    // puts(a);
    d = strlen(a);
    printf("%s", strrev(a));
    printf("%d", d);
    return 0;
}
