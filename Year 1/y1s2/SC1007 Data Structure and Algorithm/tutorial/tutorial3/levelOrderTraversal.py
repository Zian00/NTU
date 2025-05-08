class BTNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = QueueNode(data)

        # if queue is empty
        if self.head is None:
            self.head = new_node

        if self.tail:
            self.tail.next = new_node
        #  update new_node to be the tail for both empty and not empty cases
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None

        dequeued_data = self.head.data
        # update the head.next to head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return dequeued_data


def levelOrderTraversal(node):

    if node is None:
        return

    q = Queue()
    q.enqueue(node)

    while not q.is_empty():
        dequeued_item = q.dequeue()
        print(dequeued_item.item, end=" ")
        if dequeued_item.left:
            q.enqueue(dequeued_item.left)
        if dequeued_item.right:
            q.enqueue(dequeued_item.right)
    


if __name__ == "__main__":
    # Creating a sample Binary Tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = BTNode(20)
    root.left = BTNode(15)
    root.right = BTNode(50)
    root.left.left = BTNode(10)
    root.left.right = BTNode(18)
    root.right.left = BTNode(25)
    root.right.right = BTNode(80)


    print("Level-Order Traversal:")
    levelOrderTraversal(root)
