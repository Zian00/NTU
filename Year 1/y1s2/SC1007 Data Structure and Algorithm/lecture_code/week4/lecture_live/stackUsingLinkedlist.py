class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def find_node(self, index):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
            return temp

    def remove_node(self, index):
        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            prev = self.find_node(index-1)
            prev.next = prev.next.next
            # removing last node, new last node will be the node before removed node
            if index == self.size - 1:
                self.tail = prev
        self.size -= 1
        return 0

    def insert_node(self, index, value):
        if index < 0 or index > self.size:
            return -1
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node

            # if list is empty
            if self.size == 0:
                # sel.tail also need to point to the new_node when inserted
                self.tail = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.find_node(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1
        return 0


class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.ll.head.data

    def push(self, data):
        self.head = self.ll.insert_node(0, data)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        data = self.ll.head.data
        self.ll.remove_node(0)
        return data

    def is_empty(self):
        return self.ll.size == 0

    def get_size(self):
        return self.ll.size


if __name__ == "__main__":

    s = Stack()  # Create a new stack

    s.push(10)  # Push some elements: 10, 20, and 30
    s.push(20)
    s.push(30)

    print("Size:", s.get_size())  # Print the size. Should print 3

    print("Top element:", s.peek())  # Print top element. Should print 30

    print("Popped:", s.pop())  # Should print 30
    print("Popped:", s.pop())  # Should print 20

    print("New size:", s.get_size())  # Print new size. Should print 1

    # Print new top element. Should print 10
    print("New top element:", s.peek())

    # Check if empty. Should print False
    print("Is stack empty?", s.is_empty())

    print("Popped:", s.pop())  # Pop last element. Should print 10

    print("Is stack empty now?", s.is_empty())
