
class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None


def printList(head):
    print("Current List:", end=" ")
    cur = head
    while cur is not None:
        print(cur.item, end=" ")
        cur = cur.next
    print()


def findNode(head, index):
    if head is None or index < 0:
        return None
    cur = head
    while index > 0:
        cur = cur.next
        if cur is None:
            return None
        index -= 1
    return cur


def insertNode(ptrHead, index, value):
    newNode = ListNode(value)
    if ptrHead is None:
        return newNode
    if index == 0:
        newNode.next = ptrHead
        return newNode
    cur = ptrHead
    prev = None
    count = 0
    while cur is not None and count < index:
        prev = cur
        cur = cur.next
        count += 1
    if prev is not None:
        prev.next = newNode
        newNode.next = cur
    return ptrHead


def removeNode(ptrHead, index):
    # Write your code here #
    if ptrHead is None or index < 0:
        return 0

    if index == 0:
        if ptrHead.next is None:
            return 0
        else:
            ptrHead.item = ptrHead.next.item
            ptrHead = ptrHead.next
            return 1

    current = ptrHead
    count = 0
    prev = None

    while current and count < index:
        # prev stores the node before current in new iteration
        prev = current
        current = current.next
        count += 1

    if current is None:
        print("Out of range")
        return  0

    prev.next = current.next
    return 1


if __name__ == "__main__":
    head = None
    size = 0
    print("Enter one number per line (press Enter after each number).")
    print("Enter any non-digit character to finish input:")
    while True:
        try:
            item = int(input())
            head = insertNode(head, size, item)
            size += 1
        except ValueError:
            break
    printList(head)

    while True:
        try:
            index = int(input("Enter the index of the node to be removed: "))
            result = removeNode(head, index)
            if result == 1:
                size -= 1
                print("Node successfully removed")
            else:
                print("Removal failed")

            print("After the removal operation:")
            printList(head)
        except ValueError:
            break
    printList(head)
