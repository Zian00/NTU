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

    def count_words(self, node):
        # add your implementations
        count =0
        queue = Queue()
        queue.enqueue(node)

        while not queue.is_empty():
            dequeued_node = queue.dequeue()
            # end of word, count + 1
            if dequeued_node.is_end_of_word:
                count  += 1
            
            # else loop through the child and siblings
            child = dequeued_node.first_child
            while child:
                queue.enqueue(child)
                child = child.next_sibling
        
        return count

    def count_words_recursive(self, node):
        if node.is_end_of_word:
            count = 1
        else:
            count =0
        child = node.first_child
        while child:
            count += self.count_words_recursive(child)
            child = child.next_sibling
        return count


if __name__ == "__main__":
    trie = Trie()
    # Sample words to insert into the trie
    words = ["cat", "car", "cart", "dog", "dove"]
    for word in words:
        trie.insert(word)
    
    # Print the total number of words in the trie.
    # Note: count_words should count the words from the given node.
    total_words = trie.count_words(trie.root)
    print("Total words in trie:", total_words)

    total_words_recursive = trie.count_words_recursive(trie.root)
    print("Total words in trie recursive:", total_words_recursive)
