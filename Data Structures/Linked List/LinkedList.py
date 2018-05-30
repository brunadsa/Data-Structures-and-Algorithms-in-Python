"""Creating a type class call Node
Two parts:
    First part contains the value
    Second part contains the pointer for the next Node"""


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


"""Creating a type class call LinkedList
Two parts:
    First is a pointer for the list head
    Second part, optional, is the size of the list"""


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, value):  # O(1)
        self.size += 1
        newNode = Node(value)  # instance the class Node for create a new Node

        if not self.head:  # if isn't have a head
            self.head = newNode  # head pointer points to newNode
        else:  # else
            newNode.next = self.head  # nextNode pointer of the newNode
            # points to the Node what the head had have point
            self.head = newNode  # In the end, it updates the head for a newNode

    def size1(self):  # O(1)
        return self.size

    @property
    def size2(self):  # O(N), it isn't good!!!

        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.next

        return size

    def insertEnd(self, value):  # O(N)

        self.size += 1
        newNode = Node(value)
        actualNode = self.head

        if not self.head:  # if isn't have a head
            self.head = newNode  # head pointer points to newNode
        else:
            while actualNode.next is not None:
                actualNode = actualNode.next

            actualNode.next = newNode

    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:
            print("%d" % actualNode.value)
            actualNode = actualNode.next

    def remove(self, value):

        if self.head is None:
            return

        self.size += 1

        currentNode = self.head
        previousNode = None

        while currentNode.value != value:
            previousNode = currentNode
            currentNode = currentNode.next

        if previousNode is None:
            self.head = currentNode.next
        else:
            previousNode.next = currentNode.next



ListA = LinkedList()
ListA.insertStart(1)
ListA.insertStart(2)
ListA.insertStart(3)
ListA.insertStart(4)
ListA.insertStart(5)
ListA.insertEnd(6)
ListA.traverseList()

print(ListA.size1())
print("Removendo o 3")
ListA.remove(3)
ListA.traverseList()