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
    
    def print_stack(self):
        tmp_stack = Stack()
        print("The resulting stack is:", end=" ")
        while not self.is_empty():
            item = self.pop()
            print(item, end=" ")
            tmp_stack.push(item)
        # putting back into original stack
        while not tmp_stack.is_empty():
            self.push(tmp_stack.pop())
        print()



class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def getFront(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            # self.front will point to new_node, self.rear will point to new_node also
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        dequeued_node = self.front
        self.front = self.front.next
        # when dequeueing list with one node, update self.rear pointer to None
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeued_node.data

    def is_empty(self):
        return self.front == None

    def get_size(self):
        return self.size


def reverseStack(stack):
    q = Queue()
    while not stack.is_empty():
        q.enqueue(stack.pop())
    while not q.is_empty():
        stack.push(q.dequeue())
    return stack
    


if __name__ == "__main__":

    s = Stack()
    print("""1: Insert an integer into the stack;\n2: Reverse the stack;\n0: Quit;\n""")
    while True:
        
        choice = input("Please input your choice(1/2/0): ")
        if (choice == "1"):
            valueToInsert = input("Input an integer that you want to insert into the stack: ")
            s.push(valueToInsert)
            s.print_stack()
            print()
        elif(choice == "2"):
            ss= reverseStack(s)
            ss.print_stack()
        elif(choice =="0"):
            exit()
