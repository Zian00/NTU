class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None


def insert(root, data):
    if root is None:
        return BSTNode(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def push(stack, node):
    temp = StackNode(node)
    if stack.top is None:
        stack.top = temp
        temp.next = None
    else:
        temp.next = stack.top
        stack.top = temp


def pop(stack):
    if stack.top is not None:
        temp = stack.top
        stack.top = temp.next
        return temp.data
    return None


def is_empty(stack):
    return stack.top is None


def postOrderIterativeS2(root):
    # Write your code here #
    if root is None:
        return

    stack1 = Stack()
    stack2 = Stack()

    # push root to stack1
    push(stack1, root)

    # loop when stack1 is not empty
    while not is_empty(stack1):
        #  pop stack1 item and push it to stack2
        popped_node_s1 = pop(stack1)
        push(stack2, popped_node_s1)

        # if popped item.left exist, push popped item.left to stack1
        # if popped item.right exist, push popped item.right to stack1
        # in this way, left items would be below right items in stack 
        # then when pushing into stack2, right item will be below left items
        if popped_node_s1.left:
            push(stack1, popped_node_s1.left)
        if popped_node_s1.right:
            push(stack1, popped_node_s1.right)
    #  after pushing everything into stack1, start looping stack2
    while not is_empty(stack2):
        # pop from stack2 one by one, which will pop left item follow by right item then centre
        pop_node_s2= pop(stack2)
        print(pop_node_s2.data, end=" ")


if __name__ == "__main__":
    root = None
    choice = 1

    print("1: Insert an integer into the binary search tree")
    print("2: Print the post-order traversal of the binary search tree")
    print("0: Quit")

    while choice != 0:
        choice = int(input("\nPlease input your choice(1/2/0): "))

        if choice == 1:
            value = int(input("Input an integer to insert: "))
            root = insert(root, value)
        elif choice == 2:
            print("Post-order traversal: ", end="")
            postOrderIterativeS2(root)
            print()
        elif choice == 0:
            break
        else:
            print("Choice unknown")
