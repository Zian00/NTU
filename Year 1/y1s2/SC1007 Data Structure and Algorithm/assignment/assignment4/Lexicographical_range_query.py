"""
input:
5 3
cat
car
care
camera
dog
car cart
a d
care care

output :
2 
4 
1 
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0


class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.first_child = None
        self.next_sibling = None
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _find_child(self, node, char):
        prev = None
        curr = node.first_child
        while curr and curr.char < char:
            prev = curr
            curr = curr.next_sibling
        if curr and curr.char == char:
            return curr
        return None

    def _insert_child(self, node, char):
        prev = None
        curr = node.first_child
        while curr and curr.char < char:
            prev = curr
            curr = curr.next_sibling

        if curr and curr.char == char:
            return curr  # already exists

        new_node = TrieNode(char)
        new_node.next_sibling = curr
        if prev:
            prev.next_sibling = new_node
        else:
            node.first_child = new_node
        return new_node

    def search(self, word):
        node = self.root
        for char in word:
            node = self._find_child(node, char)
            if not node:
                return False  # Character path not found
        return node.is_end_of_word

    def insert(self, word):
        current = self.root
        for char in word:
            child = self._insert_child(current, char)
            current = child
        current.is_end_of_word = True


def count_in_range(trie, L, R):
    # add your implementations
    
    count = 0
    stack = Stack()
    stack.push((trie.root, ""))

    while not stack.is_empty():
        popped_node, prefix = stack.pop()
        if popped_node.is_end_of_word is True and L <= prefix <= R:
            count += 1

        child = popped_node.first_child
        siblings = []
        # collect all siblings of this child
        while child:
            siblings.append(child)
            child = child.next_sibling

        for sibling in reversed(siblings):
            stack.push((sibling, prefix + sibling.char))

    return count


def count_in_rangeQ(trie, L, R):
    queue = Queue()
    queue.enqueue((trie.root, ""))
    count = 0

    while not queue.is_empty():
        node, prefix = queue.dequeue()

        if node.is_end_of_word and L <= prefix <= R:
            count += 1

        # Traverse through children
        child = node.first_child

        while child:
            queue.enqueue((child, prefix + child.char))
            child = child.next_sibling

    return count


n, q = map(int, input().split())
trie = Trie()

# Insert words
for _ in range(n):
    word = input().strip()
    trie.insert(word)

# Process queries
for _ in range(q):
    L, R = input().strip().split()
    print(f"[OUTPUT] {count_in_range(trie, L, R)}")
    print(f"[OUTPut] {count_in_rangeQ(trie, L, R)}")
    print()
