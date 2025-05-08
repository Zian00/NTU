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

    def printQueue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()  # New line


def reverse_queue(queue):
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())
    while not stack.is_empty():
        queue.enqueue(stack.pop())

    return queue


if __name__ == "__main__":
    queue = Queue()

    # Enqueue three values
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    # Print original queue
    print("Original Queue:", end=" ")
    queue.printQueue()  # Print: 10 20 30

    # Reverse the queue
    queue = reverse_queue(queue)

    # Print reversed queue
    print("Reversed Queue:", end=" ")
    queue.printQueue()  # Print: 30 20 10
