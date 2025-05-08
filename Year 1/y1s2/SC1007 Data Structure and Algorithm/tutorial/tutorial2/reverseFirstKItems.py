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

    def print_queue(self):
        tmp_queue = Queue()
        print("The resulting queue is:", end=" ")
        while not self.is_empty():
            item = self.dequeue()
            print(item, end=" ")
            tmp_queue.enqueue(item)
        while not tmp_queue.is_empty():
            self.enqueue(tmp_queue.dequeue())
        print()




def reverse_first_k_items(queue, k):
    s = Stack()
    if k <=0 or queue.is_empty() :
        return queue
    
    for i in range(k):
        s.push(queue.dequeue())
    
    while not s.is_empty():
        queue.enqueue(s.pop())
    
    for i in range(queue.get_size()- k):
        queue.enqueue(queue.dequeue())
    return queue

if __name__ == "__main__":

    q = Queue()
    print("""1: Insert an integer into the queue;\n2: Reverse the elements of the queue until the given number;;\n0: Quit;\n""")
    while True:
        
        choice = input("Please input your choice(1/2/0): ")
        if (choice == "1"):
            valueToInsert = input("Input an integer that you want to insert into the queue: ")
            q.enqueue(valueToInsert)
            q.print_queue()
            
            print()
        elif(choice == "2"):
            reverseUntil = input("Enter an integer to reverse the queue until that number: ")
            qq = reverse_first_k_items(q, int(reverseUntil))
            qq.print_queue()
        elif(choice =="0"):
            exit()
