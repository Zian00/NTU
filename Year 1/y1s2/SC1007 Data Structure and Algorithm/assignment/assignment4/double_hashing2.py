import sys
from io import StringIO
TABLESIZE = 37
PRIME = 13
EMPTY = 0
USED = 1
DELETED = 2


class HashSlot:
    def __init__(self):
        self.key = 0
        self.indicator = EMPTY


def hash1(key):
    return key % TABLESIZE


def hash2(key):
    return (key % PRIME) + 1


def hash_insert(key, hash_table):
    """
    return -1 when inserting  duplicate key
    return number of key comparisons
    """
    h1 = hash1(key)
    h2 = hash2(key)

    comparison = 0
    first_deleted_index = None

    for i in range(TABLESIZE):
        index = (h1 + i * h2) % TABLESIZE
        slot = hash_table[index]

        # duplicate key found                                           
        if slot.indicator == USED:
            comparison += 1
            if slot.key == key:
                return -1

        elif slot.indicator == DELETED:
            # If we find a DELETED slot and haven't recorded a deleted slot yet, we save its index.
            if first_deleted_index is None:
                first_deleted_index = index

        else:
            # there's EMPTY slot
            if first_deleted_index is not None:
                hash_table[first_deleted_index].key = key
                hash_table[first_deleted_index].indicator = USED
            else:
                hash_table[index].key = key
                hash_table[index].indicator = USED
            return comparison

    if first_deleted_index is not None:
        hash_table[first_deleted_index].key = key
        hash_table[first_deleted_index].indicator = USED
        return comparison

    return comparison


def hash_delete(key, hash_table):
    """
    return -1 when key not exist to delete
    return number of key comparisons
    """
    h1 = hash1(key)
    h2 = hash2(key)

    comparison = 0
    print()

    for i in range(TABLESIZE):
        index = (h1 + i * h2) % TABLESIZE
        slot = hash_table[index]

        if slot.indicator == USED:
            comparison += 1
            if slot.key == key:
                slot.indicator = DELETED
                return comparison

        elif slot.indicator == EMPTY:
            return -1
    # after all scan but not found
    return -1


def run_test(test_name, commands):
    print(f"\n=== Running Test: {test_name} ===")

    # Redirect stdout to capture output
    original_stdout = sys.stdout
    sys.stdout = StringIO()

    # Initialize hash table
    hash_table = [HashSlot() for _ in range(TABLESIZE)]

    # Execute commands
    for cmd in commands:
        action_type = cmd[0]

        if action_type == "insert":
            key = cmd[1]
            result = hash_insert(key, hash_table)
            if result == -1:
                print(f"Insert {key}: Duplicate key")
            else:
                print(f"Insert {key}: {result} comparisons")

        elif action_type == "delete":
            key = cmd[1]
            result = hash_delete(key, hash_table)
            if result == -1:
                print(f"Delete {key}: Key not found")
            else:
                print(f"Delete {key}: {result} comparisons")

        elif action_type == "print":
            print("Hash Table Contents:")
            for i in range(TABLESIZE):
                status = "EMPTY"
                if hash_table[i].indicator == USED:
                    status = "USED"
                elif hash_table[i].indicator == DELETED:
                    status = "DELETED"
                print(f"Slot {i}: Key={hash_table[i].key}, Status={status}")

    # Get output and restore stdout
    output = sys.stdout.getvalue()
    sys.stdout = original_stdout

    print(output)
    print(f"=== Test: {test_name} Completed ===\n")


# Test Case 1: Basic Insert and Print
test1 = [
    ("insert", 5),
    ("insert", 42),
    ("insert", 79),
    ("print", None)
]

# Test Case 2: Insert with Collisions
test2 = [
    ("insert", 0),
    ("insert", 37),  # hash1(37) = 0, will collide with key 0
    ("insert", 74),  # hash1(74) = 0, will collide again
    ("print", None)
]

# Test Case 3: Delete and Try to Delete Again
test3 = [
    ("insert", 5),
    ("insert", 42),
    ("delete", 42),
    ("delete", 42),  # Try to delete again, should not find
    ("print", None)
]

# Test Case 4: Insert, Delete, then Insert at Deleted Location
test4 = [
    ("insert", 5),
    ("insert", 42),
    ("delete", 42),
    ("insert", 79),  # Should reuse the deleted slot if it's on the probe path
    ("print", None)
]

# Test Case 5: Fill Table to Near Capacity
test5 = []
# Add 35 entries (leaving 2 slots free)
for i in range(35):
    test5.append(("insert", i*10))
test5.append(("print", None))

# Test Case 6: Keys That Hash to the Same Slot
test6 = [
    ("insert", 0),
    ("insert", 37),  # hash1(37) = 0
    ("insert", 74),  # hash1(74) = 0
    ("insert", 111),  # hash1(111) = 0
    ("delete", 37),
    ("insert", 148),  # hash1(148) = 0, should reuse deleted slot
    ("print", None)
]

# Test Case 7: Duplicate Keys
test7 = [
    ("insert", 123),
    ("insert", 123),  # Duplicate, should be detected
    ("insert", 456),
    ("insert", 456),  # Another duplicate
    ("print", None)
]

# Test Case 8: Complex Scenario - Filling, Deleting, and Reinserting
test8 = []
# Fill with a specific pattern
for i in range(20):
    test8.append(("insert", i*50))
# Delete several keys
for i in range(5):
    test8.append(("delete", i*50))
# Insert some new keys
for i in range(10):
    test8.append(("insert", 1000+i))
test8.append(("print", None))

# Test Case 9: Testing Full Table and Deleted Slot Reuse
test9 = []
# Fill the entire table
for i in range(TABLESIZE):
    test9.append(("insert", 1000+i))
# Delete one entry
test9.append(("delete", 1005))
# Try to insert a new key (should use the deleted slot)
test9.append(("insert", 2000))
test9.append(("print", None))

# Run all test cases
run_test("Basic Insert and Print", test1)
run_test("Insert with Collisions", test2)
run_test("Delete and Try to Delete Again", test3)
run_test("Insert at Deleted Location", test4)
run_test("Fill Table to Near Capacity", test5)
run_test("Keys That Hash to the Same Slot", test6)
run_test("Duplicate Keys", test7)
run_test("Complex Scenario", test8)
run_test("Full Table and Deleted Slot Reuse", test9)
