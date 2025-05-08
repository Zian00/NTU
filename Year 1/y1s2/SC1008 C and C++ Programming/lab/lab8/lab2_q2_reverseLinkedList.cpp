///////// Student Info/////////
//
//           Your Name: Zheng Mian
//      Your NTU Email: zhen0158@e.ntu.edu.sg
//
//
//

#include <iostream>
#include <string>
using namespace std;

struct StringNode
{
    string name;
    StringNode *next;
};

void destroyList(StringNode *&head)
{
    StringNode *nodePtr = head; // Start at head of list
    StringNode *garbage = nullptr;

    while (nodePtr != nullptr)
    {
        // garbage keeps track of node to be deleted
        garbage = nodePtr;
        // Move on to the next node, if any
        nodePtr = nodePtr->next;
        // Delete the "garbage" node
        delete garbage;
        garbage = nullptr;
    }
    head = nullptr;
}

void printLinkedList(const StringNode *head)
{
    const StringNode *current = head;
    while (current != nullptr)
    {
        cout << current->name;
        if (current->next != nullptr)
        {
            cout << " -> ";
        }
        current = current->next;
    }
    cout << endl;
}

void insertNode2ListEnd(StringNode *&head, const string &newName)
{
    StringNode *newNode = new StringNode;
    newNode->name = newName;
    newNode->next = nullptr;

    if (head == nullptr)
    {
        head = newNode;
        return;
    }

    StringNode *temp = head;
    while (temp->next != nullptr)
    {
        temp = temp->next;
    }
    temp->next = newNode;
}

// Function to reverse the linked list
void reverseLinkedList(StringNode *&head)
{
    // TO-DO: WRITE YOUR CODE HERE

    StringNode *curr = head;
    StringNode *prev = nullptr;
    StringNode *next = nullptr;

    if (curr == nullptr)
    {
        return;
    }

    while (curr)
    {
        // store current next pointer to next
        next = curr->next;
        // point current next to prev node
        curr->next = prev;

        // move pre and curr to the next pair
        prev = curr;
        curr = next;
    }
    head = prev;
}

int main()
{
    StringNode *head = nullptr; // Initialize an empty linked list

    /////// Case 1 ////////////
    // Print the original linked list
    cout << "Original Linked List: ";
    printLinkedList(head);
    // Reverse the linked list
    reverseLinkedList(head);
    // Print the reversed linked list
    cout << "Reversed Linked List: ";
    printLinkedList(head);
    cout << endl;

    /////// Case 2 ////////////
    insertNode2ListEnd(head, "Michael");
    cout << "Original Linked List: ";
    printLinkedList(head);
    // Reverse the linked list
    reverseLinkedList(head);
    // Print the reversed linked list
    cout << "Reversed Linked List: ";
    printLinkedList(head);
    cout << endl;

    /////// Case 3 ////////////
    insertNode2ListEnd(head, "Emily");
    insertNode2ListEnd(head, "James");
    insertNode2ListEnd(head, "William");
    // Print the original linked list
    cout << "Original Linked List: ";
    printLinkedList(head);
    // Reverse the linked list
    reverseLinkedList(head);
    // Print the reversed linked list
    cout << "Reversed Linked List: ";
    printLinkedList(head);
    cout << endl;

    destroyList(head);
    return 0;
}
