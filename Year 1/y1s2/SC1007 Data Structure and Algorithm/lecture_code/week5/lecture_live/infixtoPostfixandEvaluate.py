class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        popped = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped

    def peek(self):
        return None if self.is_empty() else self.top.data

    def is_empty(self):
        return self.size == 0

class Conversion:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.stack = Stack()

    def is_operand(self, char):
        return char.isdigit()

    def has_higher_precedence(self, op1, op2):
        if op1 == '^' and op2 == '^':
            return False
        return self.precedence.get(op1, 0) >= self.precedence.get(op2, 0)

    def infix_to_postfix(self, expression):
        postfix = []
        self.stack = Stack()

        expression += ')'
        self.stack.push('(')

        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                num = ''
                while i < len(expression) and expression[i].isdigit():
                    num += expression[i]
                    i += 1
                postfix.append(num)
                continue  # Skip the increment at the end of loop
            elif expression[i] == '(':
                self.stack.push(expression[i])
            elif expression[i] == ')':
                while not self.stack.is_empty() and self.stack.peek() != '(':
                    postfix.append(self.stack.pop())
                self.stack.pop()
            else:
                while (not self.stack.is_empty() and self.stack.peek() != '(' and
                       self.has_higher_precedence(self.stack.peek(), expression[i])):
                    postfix.append(self.stack.pop())
                self.stack.push(expression[i])
            i += 1

        while not self.stack.is_empty():
            postfix.append(self.stack.pop())

        return ' '.join(postfix[:-1])

    def evaluate_postfix(self, postfix):
        self.stack = Stack()
        tokens = postfix.split()

        for token in tokens:
            if token.isdigit():
                self.stack.push(int(token))
            else:
                val2 = self.stack.pop()
                val1 = self.stack.pop()

                if token == '+':
                    self.stack.push(val1 + val2)
                elif token == '-':
                    self.stack.push(val1 - val2)
                elif token == '*':
                    self.stack.push(val1 * val2)
                elif token == '/':
                    self.stack.push(val1 / val2)
                elif token == '^':
                    self.stack.push(val1 ** val2)

        return self.stack.pop()

if __name__ == "__main__":
    obj = Conversion()
    exp = input("Enter infix expression: ")
    postfix = obj.infix_to_postfix(exp)
    print(f"Postfix expression: {postfix}")
    result = obj.evaluate_postfix(postfix)
    print(f"Result: {result}")