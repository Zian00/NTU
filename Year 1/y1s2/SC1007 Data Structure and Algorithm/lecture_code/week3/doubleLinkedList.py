class Link():
    def __init__(self, datum, next=None, previous=None):
        self.__data = datum
        self.__next = next
        self.__previous = previous

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def getPrevious(self):
        return self.__previous

    def setData(self, d):
        self.__data = d

    def setNext(self, link):
        if link is None or isinstance(link, Link):
            self.__next = link
        else:
            raise Exception("Next link must be Link or None")

    def setPrevious(self, link):
        if link is None or isinstance(link, Link):
            self.__previous = link
        else:
            raise Exception("Previous link must be Link or None")

    def isFirst(self):
        return self.getPrevious() is None

    def isLast(self):
        return self.getNext() is None


# Create individual links
link1 = Link(datum=1)
link2 = Link(datum=2)
link3 = Link(datum=3)

# Link them together
link1.setNext(link2)
link2.setPrevious(link1)
link2.setNext(link3)
link3.setPrevious(link2)

# Access data and links
print(link1.getData())  # Output: 1
print(link1.getNext().getData())  # Output: 2
print(link2.getPrevious().getData())  # Output: 1
print(link2.getNext().getData())  # Output: 3
print(link3.getPrevious().getData())  # Output: 2
print(link3.getNext())

# None <- Node1 <-> Node2 <-> Node3 -> None
