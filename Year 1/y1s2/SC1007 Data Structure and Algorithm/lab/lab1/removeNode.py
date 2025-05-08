class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, index=None):

        new_node = Node(data)
        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            return True

        if index is not None:
            current = self.head
            count = 0
            while current and count < index - 1:
                current = current.next
                count += 1

            if current is None:
                print("Index out of range")
                return False

            new_node.next = current.next
            current.next = new_node
            return True
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            return True

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" => ")
            current = current.next
        print("None")


def removeNode(ptrHead, index):
    if ptrHead is None or index < 0:

        return 0

    if index == 0:
        return ptrHead.next, 1

    current = ptrHead
    count = 0
    prev = None

    while current and count < index:
        # prev stores the node before current in new iteration
        prev = current
        current = current.next
        count += 1

    if current is None:
        print("Out of range")
        return ptrHead, 0

    prev.next = current.next
    return ptrHead, 1


ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.display()

removeNode(ll.head, 1)
ll.display()
