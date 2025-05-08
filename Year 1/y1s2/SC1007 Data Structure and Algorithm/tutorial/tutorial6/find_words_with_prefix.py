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


class TrieNode:
    def __init__(self, char=''):
        self.char = char
        self.is_end_of_word = False
        self.first_child = None
        self.next_sibling = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _find_child(self, node, char):
        curr = node.first_child
        while curr:
            if curr.char == char:
                return curr
            curr = curr.next_sibling
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

    def insert(self, word):
        current = self.root
        for char in word:
            current = self._insert_child(current, char)
        current.is_end_of_word = True

    def find_words_with_prefix(self, node, prefix):
        stack = Stack()
        results = []

        stack.push((node, prefix))
        while not stack.is_empty():
            popped_node, popped_prefix = stack.pop()

            # end of word, push to results list
            if popped_node.is_end_of_word:
                results.append(popped_prefix)
            # not end of word, traverse to child of next level
            child = popped_node.first_child

            while child:
                stack.push((child, popped_prefix + child.char))
                child = child.next_sibling
        return results



    """
    Tutorial Solution
    """
    def find_words_with_prefix_solution(self, node, prefix):

        # Use a list to collect the words
        results = []
        node = self.root
        # Step 1: Traverse the Trie to the node
        # matching the prefix
        for char in prefix:
            node = self._find_child(node, char)
            if not node:
                return []

        # Step2: Perform dfs to collect all complete words
            self.collect_all_words_dfs(node, prefix, results)
        return results

    def print_all_words_dfs(self, node, prefix):
        if node.is_end_of_word:
            print(prefix)
        child = node.first_child
        while child:
            self. print_all_words(child, prefix+child.char)
            child = child.next_sibling

    def collect_all_words_dfs(self, node, current_prefix, results):
        """
        Recursively collects all words starting from the given node.

        Args:
            node: The current TrieNode to explore from.
            current_prefix: The string built so far to reach this node.
            results: A list to append found words to.
        """
        # Base case / Action: If the current node marks the end of a word,
        # add the constructed prefix to the results list.
        if node.is_end_of_word:
            results.append(current_prefix)

        # Recursive step: Explore all children of the current node.
        child = node.first_child
        while child:
            # Recursively call for each child, appending the child's character
            # to the current prefix.
            self.collect_all_words_dfs(
                child, current_prefix + child.char, results)
            # Move to the next sibling.
            child = child.next_sibling


if __name__ == "__main__":
    trie = Trie()
    # Sample words to insert into the trie
    words = ["cat", "cap", "car", "dog", "doll", "door"]
    for word in words:
        trie.insert(word)

    # Sample prefixes to search
    sample_prefixes = ["ca", "do", "z"]

    for prefix in sample_prefixes:
        node = trie.root
        found = True
        for char in prefix:
            node = trie._find_child(node, char)
            if not node:
                found = False
                break
        if not found:
            print(f"No words with prefix '{prefix}'")
        else:
            found_words = trie.find_words_with_prefix(node, prefix)
            print(f"Words with prefix '{prefix}': {found_words}")
