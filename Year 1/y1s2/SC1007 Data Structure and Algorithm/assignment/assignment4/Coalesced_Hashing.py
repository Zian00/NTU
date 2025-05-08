TABLESIZE = 37
PRIME = 13
EMPTY = 0
USED = 1


class HashSlot:
    def __init__(self):
        self.key = 0
        self.indicator = EMPTY
        self.next = -1


def hash_func(key):
    return key % TABLESIZE


def hash_insert(key, hash_table):
    # write your codes here
    """
    return -1 for inserting duplicate key
    return value larger than table size means table is full
    """

    index = hash_func(key)

    # slot is empty, insert directly
    if hash_table[index].indicator == EMPTY:
        hash_table[index].key = key
        hash_table[index].indicator = USED
        return index

    # slot is occupied, check for duplicate while traversing
    current = index
    while current != -1:
        if hash_table[current].key == key:
            return -1 # duplicate found, return -1
        current = hash_table[current].next
    
    # find the next available slot using linear probing to insert
    for i in range(TABLESIZE):
        probe = (index + i) % TABLESIZE
        if hash_table[probe].indicator == EMPTY:
            hash_table[probe].key = key
            hash_table[probe].indicator = USED
            hash_table[current].next = probe # link the prev node, which is current to the new node
            return probe
    return TABLESIZE 


def hash_find(key, hash_table):
    # write your codes here
    """
    return -1 when finding non-existing key
    """
    index = hash_func(key)
    current = index
    while current != -1:
        if hash_table[current].key == key:
            return current
        current = hash_table[current].next

    return -1        


def print_menu():
    print("============= Hash Table ============")
    print("|1. Insert a key to the hash table  |")
    print("|2. Search a key in the hash table  |")
    print("|3. Print the hash table            |")
    print("|4. Quit                            |")
    print("=====================================")
    print("Enter selection: ", end="")


def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))

    hash_table = [HashSlot() for _ in range(TABLESIZE)]
    for slot in hash_table:
        slot.key = 0
        slot.indicator = EMPTY
        slot.next = -1

    i = 0
    print_menu()
    while i < len(data):

        opt = data[i]
        i += 1

        if opt == 1:  # Insert
            print("Enter a key to be inserted:")
            if i >= len(data):
                break
            key = data[i]
            i += 1
            index = hash_insert(key, hash_table)
            if index < 0:
                print("Duplicate key")
            elif index < TABLESIZE:
                print(f"Insert {key} at index {index}")
            else:
                print("Table is full.")
            print("Enter selection: ", end="")
        elif opt == 2:  # Search
            print("Enter a key for searching in the HashTable:")
            if i >= len(data):
                break
            key = data[i]
            i += 1
            index = hash_find(key, hash_table)
            if index != -1:
                print(f"{key} is found at index {index}.")
            else:
                print(f"{key} is not found.")
            print("Enter selection: ", end="")
        elif opt == 3:  # Print table
            print("index:\t key \t next")
            for j in range(TABLESIZE):
                print(f"{j}\t{hash_table[j].key}\t{hash_table[j].next}")
            print("Enter selection: ", end="")
        elif opt == 4:
            break
        else:
            print("Enter selection: ", end="")
            continue


if __name__ == "__main__":
    main()
