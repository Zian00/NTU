class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def pre_order_traversal(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")


if __name__ == "__main__":
    # Creating a sample tree:
    #         1
    #       /  \
    #      2    3
    #    / \   /  \
    #   4  5  6   7

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Pre-Order Traversal:")
    root.pre_order_traversal(root)
    print("\nIn-Order Traversal:")
    root.in_order_traversal(root)
    print("\nPost-Order Traversal:")
    root.post_order_traversal(root)
