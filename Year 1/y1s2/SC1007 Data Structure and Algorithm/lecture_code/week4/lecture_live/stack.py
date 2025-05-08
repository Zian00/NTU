class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data

    def push(self, data):
        new_node = Node(data)
        
        # push from top or front
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop: Empty stack")
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data
    
    def is_empty(self):
        #  returns True or False
        return self.top is None
    
    def get_size(self):
        return self.size
    

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Size:", s.get_size())

    print("Top element:", s.peek())

    print("Popped:", s.pop())
    print("Popped:", s.pop())

    print("New size:", s.get_size())
    print("New top element:", s.peek())

    print("Is stack empty ?", s.is_empty())

    print("Popped:", s.pop())

    print("Is stack empty now ?", s.is_empty())

