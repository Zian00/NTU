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


def move_max_to_front(ll: LinkedList):
    if ll.head is None or ll.head.next is None:
        return

    max_node = ll.head
    max_node_prev = None
    current = ll.head

    while current.next:
        if current.next.data > max_node.data:
            max_node = current.next
            max_node_prev = current
        current = current.next

    if max_node != ll.head:
        if max_node_prev:
            # Adjust the pointer of max_node_prev to skip over max_node in the list.
            # This effectively removes max_node from its original position.
            max_node_prev.next = max_node.next
        max_node.next = ll.head
        ll.head = max_node


"""
    def moveMaxFront(self):
        if self.head is None or self.head.next is None:
            return
        max_node = self.head
        max_node_prev = None
        current = self.head

        while current.next:
            # check if data of next node > current node
            if current.next.data > max_node.data:
                # current.next is updated to max_node
                max_node = current.next
                # current is updated to max_mode_prev
                max_node_prev = current
            # current.next is then assigned to current
            current = current.next

        if max_node != self.head:
            if max_node_prev:
                # Adjust the pointer of max_node_prev to skip over max_node in the list.
                # This effectively removes max_node from its original position.
                max_node_prev.next = max_node.next
            #head of list is assigned to max_node.next
            max_node.next = self.head
            # then assign max_node to the head
            self.head = max_node
"""

ll = LinkedList()

print(f"1: Insert an integer to the linked list:\n2: Move the node with the largest stored value to the front of the list:\n0: Quit:\n")

while (1):
    userInputChoice = input("Please input your choice (1/2/0): ")
    if (userInputChoice == "1"):
        userInputValue = input(
            "Input an integer that you want to add to the linked list: ")
        ll.insert_at_back(int(userInputValue))
        print("The Linked List is: ")
        ll.display()
    elif (userInputChoice == "2"):
        move_max_to_front(ll)
        print("The resulting Linked List is: ")
        ll.display()
    elif (userInputChoice == "0"):
        break
