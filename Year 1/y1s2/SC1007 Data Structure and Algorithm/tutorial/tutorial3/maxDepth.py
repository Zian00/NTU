class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def pre_order_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")

def maxDepth(node):
    if node is None:
        return -1w
    return 1 + max(maxDepth(node.left), maxDepth(node.right))


if __name__ == "__main__":

    root = Node(50)
    root.left = Node(20)
    root.right = Node(60)
    root.left.left = Node(10)
    root.left.right = Node(30)
    root.right.right = Node(80)
    root.left.right.left = Node(55)

    print("Pre-Order Traversal:")
    root.pre_order_traversal(root)

    print("\nIn-Order Traversal:")
    root.in_order_traversal(root)

    print("\nPost-Order Traversal:")
    root.post_order_traversal(root)

    print("\nTotal number of nodes in the tree:", maxDepth(root))
