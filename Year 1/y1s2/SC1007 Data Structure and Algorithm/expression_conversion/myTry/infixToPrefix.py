# Define operator precedence globally
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


class Node:
    def __init__(self, data):
        # Initialize a node with data and null next pointer
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        # Initialize an empty stack with no elements
        self.top = None
        self.size = 0

    def push(self, data):
        # Add a new element to the top of the stack
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        # Remove and return the top element of the stack
        if self.is_empty():
            return None
        popped = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped

    def peek(self):
        # Return the top element without removing it
        return None if self.is_empty() else self.top.data

    def is_empty(self):
        # Check if the stack has no elements
        return self.size == 0


def is_operand(char):
    # Check if a character is a letter or digit
    return char.isalnum()


def has_higher_precedence(op1, op2, precedence=PRECEDENCE):
    # Compare precedence of two operators using the global precedence
    return precedence.get(op1, 0) >= precedence.get(op2, 0)


def infix_to_prefix(expression):

    reversed_exp = ""
    output = ""
    operator_stack = Stack()
    i=0

    # reverse the expression to make it work like postfix
    for char in reversed(expression):
        if char == '(':
            reversed_exp += ')'
        elif char == ')':
            reversed_exp += '('
        
        else:
            reversed_exp += char

    while i < len(reversed_exp):
        char = reversed_exp[i]

        # if character is a space
        if char.isspace():
            i += 1
            continue

        if char.isalnum():
            if char.isalpha():
                output += char
            
            else:
                # if character is operand
                num = ""
                while i < len(reversed_exp) and reversed_exp[i].isdigit():
                    num += reversed_exp[i]
                    i += 1
                output += num
                i -= 1
        
        # if character is (
        elif char == '(':
            operator_stack.push(char)
        elif char == ')':
            while not operator_stack.is_empty()  and operator_stack.peek() != '(':
                output += operator_stack.pop()
            
            # if character is )
            if not operator_stack.is_empty() and operator_stack.peek() == '(':
                operator_stack.pop()

        # if character is operator
        elif char in PRECEDENCE:
            # pop from stack into output if the top of stack has higher or equl precedence than char
            while (not operator_stack.is_empty() and operator_stack.peek() != '(' and has_higher_precedence(operator_stack.peek(), char)):
                output += operator_stack.pop()
            # after handling higher-precedence operators, current operator is pushed onto stack
            operator_stack.push(char)

        i += 1

        # after processing all operators, any operators left in the stack are then appended to output
    while not operator_stack.is_empty() :
        output += operator_stack.pop()
    
    # reverse the output back to prefix
    output = output[::-1]
    
    return output



def evaluate_prefix(prefix):
    stack = Stack()
    tokens = prefix.split()

    for token in tokens[::-1]:
        if token.isdigit():
            stack.push(int(token))
        else:
            # When an operator is encountered, the first popped value is the left operand and 
            # the second popped is the right operand, matching the prefix evaluation rules.
            val1 = stack.pop()
            val2 = stack.pop()
            if token == '+':
                stack.push(val1 + val2)
            elif token == '-':
                stack.push(val1 - val2)
            elif token == '*':
                stack.push(val1 * val2)
            elif token == '/':
                stack.push(val1 / val2)
            elif token == '^':
                stack.push(val1 ** val2)

    return stack.pop()


if __name__ == "__main__":
    # Main program entry point for user interaction
    exp = input("Enter infix expression: ")
    prefix = infix_to_prefix(exp)
    print(f"Prefix expression: {prefix}")
    try:
        result = evaluate_prefix(prefix)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        print("Make sure the expression contains valid numbers and operators.")


# test with (3 + 4) * 5
# result be *+345