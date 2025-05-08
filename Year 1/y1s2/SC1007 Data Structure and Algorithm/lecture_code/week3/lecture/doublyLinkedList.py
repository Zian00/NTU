import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from doubleLinkedList import Link

class DoublyLinkedList():
    def __init__(self):
        self.__first = None
        self.__last = None

    def getFirst(self):
        return self.__first

    def getLast(self):
        return self.__last

    def setFirst(self, link):
        if link is None or isinstance(link, Link):
            self.__first = link
            if (self.__last is None or link is None):
                self.__last = link
        else:
            raise Exception("First link must be Link or None")

    def setLast(self, link):
        if link is None or isinstance(link, Link):
            self.__last = link
            if (self.__first is None or link is None):
                self.__first = link
        else:
            raise Exception("Last link must be Link or None")

    def insertFirst(self, datum):
        link = Link(datum, next=self.getFirst())

        if self.isEmpty():
            self.setLast(link)
        else:
            self.getFirst().setPrevious(link)
            self.setFirst(link)

    # insert = insertFirst

    def insertLast(self, datum):
        link = Link(datum, previous=self.getLast())
        if self.isEmpty():
            self.setFirst(link)
        else:
            self.getLast().setNext(link)
            self.setLast(link)

    def delete(self, goal, key=lambda x: x):
        link = self.find(goal, key)
        if link is None:
            raise Exception("Cannot find link to delete in list")
        if link.isLast():
            self.setLast(link.getPrevious())

            if self.getLast() is not None:
                self.getLast().setNext(None)
            else:
                self.setFirst(None)

        elif link.isFirst():
            self.setFirst(link.next())

            if self.getFirst() is not None:
                self.getFirst().setPrevious(None)
            else:
                self.setLast(None)

        else:
            link.getNext().setPrevious(link.getPrevious())
            link.getPrevious().setNext(link.getNext())
        return link.getData()

    def isEmpty(self):
        return self.__first is None

    def find(self, goal, key=lambda x: x):
        current = self.getFirst()
        while current is not None:
            if key(current.getData()) == goal:
                return current
            current = current.getNext()
        return None

    def printResult(self):
        current = self.getFirst()
        while current:
            print(current.getData(), end=" -> ")
            current = current.getNext()

print("\nprogram result start here:")
dll = DoublyLinkedList()
dll.insertFirst(10)  # List: 10
dll.insertFirst(20)  # List: 20 -> 10
dll.insertFirst(30)  # List: 30 -> 20 -> 10
dll.insertLast(40)   # List: 30 -> 20 -> 10 -> 40
dll.insertLast(50)   # List: 30 -> 20 -> 10 -> 40 -> 50
dll.printResult()
print("")

node = dll.find(20)  # Find node with value 20
if node:
    print(f"Found: {node.getData()}")  # Output: Found: 20
else:
    print("Not found.")


dll.delete(10)  # Deletes node with value 10. List: 30 -> 20 -> 40 -> 50
dll.delete(50)  # Deletes node with value 50. List: 30 -> 20 -> 40
dll.printResult()
print("")
print(dll.isEmpty())  # Output: False
