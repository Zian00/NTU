class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


def preOrderIterative(root):
    s = Stack()
    temp = root
    if temp is None:
        return
    s.push(temp)

    while not s.is_empty():
        pop_item = s.pop()
        print(pop_item.data, end=" ")
        if pop_item.right:
            s.push(pop_item.right)
        
        if pop_item.left:
            s.push(pop_item.left)


if __name__ == "__main__":
    # Creating a sample Binary Tree:
    #        20
    #       / \
    #      15   50
    #    / \   /   \
    #  10  18 25  80

    root = Node(20)
    root.left = Node(15)
    root.right = Node(50)
    root.left.left = Node(10)
    root.left.right = Node(18)
    root.right.left = Node(25)
    root.right.right = Node(80)

    print("Pre-Order Traversal:")
    preOrderIterative(root)
