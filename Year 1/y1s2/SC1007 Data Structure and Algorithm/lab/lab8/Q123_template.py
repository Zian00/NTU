class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.first_child = None
        self.next_sibling = None
        self.is_end_of_word = False


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _find_child(self, node, char):
        current = node.first_child
        while current:
            if current.char == char:
                return current
            current = current.next_sibling
        return None

    def _add_child(self, node, char):
        # add your implementations to insert a child following the alphabetical order
        prev = None
        curr = node.first_child
        # stop if reached the end or found a node with character >= char
        # loop end when curr reached the last node of value less than char in same level, then the new node can insert before curr
        while curr and curr.char < char:
            # prev keep track of previous node during traversal (to update next_sibling if needed)
            prev = curr
            curr = curr.next_sibling

        # duplicate key found
        if curr and curr.char == char:
            return curr

        new_node = TrieNode(char)
        new_node.next_sibling = curr
        if prev:
            prev.next_sibling = new_node
        else:  # if prev is None, means new_node is the new first child of the node
            node.first_child = new_node
        return new_node

    def insert(self, word):
        node = self.root
        for char in word:  # loop through the word

            # character exists, move to its child
            # else add it
            child = self._find_child(node, char)
            if not child:
                child = self._add_child(node, char)
            # move to the next level down the trie
            node = child
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = self._find_child(node, char)
            if not node:
                return False
        return node.is_end_of_word

    def print_words_alphabetically(self):
        # add you implementations
        stack = Stack()
        stack.push((self.root, ""))

        while not stack.is_empty():
            popped_node, prefix = stack.pop()

            if popped_node.is_end_of_word:
                print(prefix)

            child = popped_node.first_child
            siblings = []

            while child:
                siblings.append(child)
                child = child.next_sibling

            for sibling in reversed(siblings):
                stack.push((sibling, prefix + sibling.char))

    def print_words_reverse_alphabetically(self):
        # add your implementations
        stack = Stack()
        stack.push((self.root, ""))

        while not stack.is_empty():
            popped_node, prefix = stack.pop()
            if popped_node.is_end_of_word:
                print(prefix)

            child = popped_node.first_child
            siblings = []

            while child:
                siblings.append(child)
                child = child.next_sibling

            for sibling in siblings:
                stack.push((sibling, prefix + sibling.char))

        # Assume Trie, TrieNode, and Queue classes have already been defined.
        # Create a new Trie instance
        
trie = Trie()
trie.insert("car")
trie.insert("care")
trie.insert("cat")
trie.insert("camp")
trie.insert("camera")

trie.print_words_reverse_alphabetically()
print()
trie.print_words_alphabetically()
