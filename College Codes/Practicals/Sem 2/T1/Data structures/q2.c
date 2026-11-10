#include <stdio.h>
#include <stdlib.h>
#define max_size 5

int stack[max_size];
int arr[] = {10, 20, 30, 40};
int top = -1;

int isFull() {
    return top == max_size - 1;
}

int isEmpty() {
    return top == -1;
}

void push() {
    if (isFull()) {
        printf("Stack Overflow\n");
    } else {
        for (int i = 0; i < 4; i++) {
            stack[++top] = arr[i];
            printf("Pushed %d to stack\n", arr[i]);  
        }
    }  
}

void pop() {
    if (isEmpty()) {
        printf("Stack underflow\n");
    } else {
        int popped = stack[top]; 
        top--; 
        printf("Popped element is: %d\n", popped);
    }
}

void display() {
    if (isEmpty()) {
        printf("Stack is empty\n");
    } else {
        printf("Stack elements are:\n");
        for (int i = top; i >= 0; i--) {
            printf("%d\n", stack[i]);
        }
    }
}

int main() {
    int choice;
    while (1) {
        printf("\nStack Operations Menu\n");
        printf("1. Push\n2. Pop\n3. Display\n4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1: push();    break;
            case 2: pop();     break;
            case 3: display(); break;
            case 4: printf("Exit\n"); exit(0);
            default: printf("Invalid choice\n");
        }
    }
    return 0;
}
