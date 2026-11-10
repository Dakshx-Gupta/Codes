#include <stdio.h>
#include <stdlib.h>

// Define structure for node
struct Node {
int data;
struct Node* next;
};

// Function to create a new node
struct Node* createNode(int data) {
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->data = data;
newNode->next = NULL;
return newNode;
}

// Insert at beginning
struct Node* insertAtBeginning(struct Node* head, int data) {
struct Node* newNode = createNode(data);
newNode->next = head;
head = newNode;
return head;
}

// Insert at end
struct Node* insertAtEnd(struct Node* head, int data) {
struct Node* newNode = createNode(data);
if (head == NULL) {
return newNode;
}
struct Node* temp = head;
while (temp->next != NULL) {
temp = temp->next;
}

temp->next = newNode;
return head;
}

// Insert at a specific position (1-based index)
struct Node* insertAtPosition(struct Node* head, int data, int pos) {
struct Node* newNode = createNode(data);
if (pos == 1) {
newNode->next = head;
return newNode;
}
struct Node* temp = head;
for (int i = 1; i < pos - 1 && temp != NULL; i++) {
temp = temp->next;
}
if (temp == NULL) {
printf("Position out of range!\n");
return head;
}
newNode->next = temp->next;
temp->next = newNode;
return head;
}

// Display linked list
void display(struct Node* head) {
struct Node* temp = head;
while (temp != NULL) {
printf("%d -> ", temp->data);
temp = temp->next;
}
printf("NULL\n");
}

// Main function
int main() {
    int n, i, c, v, p;
struct Node* head = NULL;

printf("Enter number of nodes you want: ");
scanf("%d", &n);
for(i = 0; i < n; i++){
    printf("1. Begining\n");
    printf("2. Specific Position\n");
    printf("3. End\n");
    printf("Where do you want to insert the element: ");
    scanf("%d", &c);
    switch(c){
        case 1:
            printf("Enter element: ");
            scanf("%d", &v);
            head = insertAtBeginning(head, v);
            display(head);
            break;
        case 2:
            printf("Current Linked List\n");
            display(head);
            printf("Enter element: ");
            scanf("%d", &v);
            printf("Enter position: ");
            scanf("%d", &p);
            head = insertAtPosition(head, v, p);
            display(head);
            break;
        case 3:
            printf("Enter element: ");
            scanf("%d", &v);
            head = insertAtEnd(head, v);
            display(head);
            break;
        default:
            printf("Invalid choice");
            break;
    }
}
// Insert at beginning
// head = insertAtBeginning(head, 70);
// head = insertAtBeginning(head, 60);

// head = insertAtBeginning(head, 40);
// head = insertAtBeginning(head, 30);
// head = insertAtBeginning(head, 20);
// head = insertAtBeginning(head, 10);

// Insert at end
// head = insertAtEnd(head, 60);
// head = insertAtEnd(head, 70);

// Insert at position
// head = insertAtPosition(head, 15, 3);

printf("Linked List:\n");
printf("Total Nodes: %d\n", n);
display(head);
return 0;
}
