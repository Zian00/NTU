class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next
        print("")

    def insert_at_back(self, data):
        new_node = Node(data)  # Create new node with only data parameter
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


def removeDuplicatesSortedLL(ll: LinkedList):
    if ll.head is None or ll.head.next is None:
        return
    current = ll.head

    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

# def removeDuplicatesSortedLL(self):
#     if self.head is None or self.head.next is None:
#         return
#     current = self.head

#     while current.next:
#         if current.data == current.next.data:
#             current.next = current.next.next
#         current = current.next


ll = LinkedList()

print(f"1: Insert an integer to the linked list:\n2: Remove duplicates from a sorted linked list:\n0: Quit:\n")

while (1):
    userInputChoice = input("Please input your choice (1/2/0): ")
    if (userInputChoice == "1"):
        userInputValue = input(
            "Input an integer that you want to add to the linked list: ")
        ll.insert_at_back(int(userInputValue))
        print("The Linked List is: ")
        ll.display()
    elif (userInputChoice == "2"):
        removeDuplicatesSortedLL(ll)
        print("The resulting Linked List is: ")
        ll.display()
    elif (userInputChoice == "0"):
        break
