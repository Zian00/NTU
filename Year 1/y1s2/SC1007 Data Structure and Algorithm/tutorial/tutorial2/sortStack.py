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


def sort_stack(stack):
    tmp_stack = Stack()
    while not stack.is_empty():
        # store newly popped data into tmp
        tmp = stack.pop()

        # while tmp_stack is not empty and top of tmp_stack > tmp, push items in tmp_stack to stack
        while not tmp_stack.is_empty() and tmp_stack.peek() > tmp:
            stack.push(tmp_stack.pop())
        
        # push tmp into tmp_stack
        tmp_stack.push(tmp)

    # once everything sorted in temp_stack, pop back into original stack, resulting in ascending order
    while not tmp_stack.is_empty():
        stack.push(tmp_stack.pop())
    return stack

if __name__ == "__main__":

    s = Stack()
    print("""1: Insert an integer into the stack;\n2: Sort the stack in ascending order;\n0: Quit;\n""")
    while True:

        choice = input("Please input your choice(1/2/0): ")
        if (choice == "1"):
            valueToInsert = input(
                "Input an integer that you want to insert into the stack: ")
            s.push(valueToInsert)
            s.print_stack()

            print()
        elif (choice == "2"):
            sort_stack(s)
            s.print_stack()
        elif (choice == "0"):
            exit()
