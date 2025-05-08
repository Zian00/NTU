class Link(object):
    def __init__(self, datum, next=None):
        self.__data = datum  # data in the current node
        self.__next = next  # reference to the next node

    def getData(self):
        return self.__data

    def setData(self, datum):
        self.__data = datum

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next

    def isLast(self):
        return self.getNext() is None

    def __str__(self):
        return str(self.getData())


class LinkedList(object):
    def __init__(self):
        self.__first = None

    def identity(x):
        return x

    def getFirst(self):
        return self.__first

    def setFirst(self, link):
        self.__first = link

    def isEmpty(self):
        return self.getFirst() is None

    # insert at the start of list
    def insert(self, datum):
        link = Link(datum, self.getFirst())
        self.setFirst(link)

    def find(self, goal, key=identity):
        link = self.getFirst()
        while link is not None:
            # print("key here: ",key(link.getData()))
            if key(link.getData()) == goal:
                return link
            link = link.getNext()

    def insertAfter(self, goal, newDatum, key=identity):
        link = self.find(goal, key)
        if link is None:
            return False
        newLink = Link(newDatum, link.getNext()) # the next of newLink is set to link.getNext()
        link.setNext(newLink) # the next of old link is pointing to newLink
        return True

    def delete(self, goal, key=identity):
        if self.isEmpty():
            raise Exception("Cananot delete from empty list")

        previous = None
        current = self.getFirst()
        while current is not None:
            if goal == key(current.getData()):
                if previous is None:
                    self.setFirst(current.getNext())
                else:
                    previous.setNext(current.getNext())
                return current.getData()
            previous = current
            current = current.getNext()
        raise Exception("No item with matching key found in list")

    def __str__(self):
        result = "["
        link = self.getFirst()
        while link is not None:
            if len(result) > 1:
                result += " > "
            result += str(link)
            link = link.getNext()
        return result + "]"


list = LinkedList()
list.insert((3, "a"))
print(list)
list .insert((2, "b"))
print(list)
list.insert((1, "c"))
print(list)
list.insertAfter((2, "b"), (2.5, "x"))
print(list)