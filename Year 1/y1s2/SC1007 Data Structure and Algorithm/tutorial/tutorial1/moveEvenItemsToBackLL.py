class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")

    def insert_at_back(self, data):
        new_node = Node(data)  # Create new node with only data parameter
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


def move_even_items_to_back(ll):
    odd_head = odd_tail = None
    even_head = even_tail = None

    current = ll.head

    while current:
        if current.data % 2 == 0:
            if even_tail:
                # the current is assigned to eventail.next
                even_tail.next = current
                # then the eventail.next is assigned to eventail, which become the new eventail
                even_tail = even_tail.next
            else:
                # even_tail is empty, current is assign to both evenhead and eventail
                even_head = even_tail = current

        else:
            if odd_tail:    
                odd_tail.next = current
                odd_tail = odd_tail.next
            else:
                odd_head = odd_tail = current
        current = current.next

    if odd_tail:
        odd_tail.next = even_head
    if even_tail:
        even_tail.next = None

    ll.head = odd_head if odd_head else even_head


ll = LinkedList()
for value in [2, 7, 18, 3, 4, 15]:
    ll.insert_at_back(value)

ll.display()
move_even_items_to_back(ll)
ll.display()
