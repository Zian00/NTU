class Node:
    def __init__(self, data, next=None):  # Set default value for next
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def sizeList(self):
        return self.size

    def insert_at_back(self, data):
        new_node = Node(data)  # Create new node with only data parameter
        if self.head is None:
            self.head = new_node
            self.size+=1
            return
    
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.size += 1

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert(self, data, index):
        # Create a new node with the given data
        new_node = Node(data)
        # If list is empty or inserting at head
        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            return True

        # Start at the head of the list
        current = self.head
        count = 0
        # Traverse until index-1 position
        # (node before where we want to insert)
        while current and count < index - 1:
            current = current.next
            count += 1

        # If current is None, index was too large
        if current is None:
            print("Index out of range")
            return False

        # Insert the new node by updating pointers:
        # 1. New node points to current's next node
        # 2. Current node points to new node
        new_node.next = current.next
        current.next = new_node
        self.size += 1
        return True

    def insertNode(self, index, item):
        newNode = Node(item)
        if self.head is None:
            return newNode
        if index == 0:
            newNode.next = self.head
            return newNode
        prev = self.findNode(index - 1)

        if prev is not None:
            newNode.next = prev.next
            prev.next = newNode
        self.size += 1
        return self.head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def findAt(self, index):
        current = self.head
        if not current:
            return None
        while index > 0:
            current = current.next
            if not current:
                return None
            index -= 1
        return current

    def findNode(self, index):
        if self.head is None or index < 0 or index >= self.size:
            return None
        else:
            current = self.head
            while index > 0:
                current = current.next
                index -= 1
        return current


a = LinkedList()
a.insert_at_back("a")
a.insert_at_back("b")
a.insert_at_back("c")
a.insert_at_front("d")
a.display()
a.insertNode(3, "yoh")
a.display()
print(f"size of linkedlist is {a.sizeList()}")
print(f"node of index is at {a.findNode(4).data}")
# node = a.findAt(2)
# print(node.data)

# a.display()
