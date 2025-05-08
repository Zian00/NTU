class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


if __name__ == "__main__":

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Front element before dequeue:", queue.getFront())
    print("Size before dequeue:", queue.get_size())
    print("Dequeued element:", queue.dequeue())
    print("Front element after dequeue:", queue.getFront())
    print("Size after dequeue:", queue.get_size())
