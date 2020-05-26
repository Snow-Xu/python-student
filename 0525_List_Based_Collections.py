


#array

# linked list
#node object
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    def getValue(self):
        return self.value
    def getNext(self):
        return self.next
#linked list:
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    def printList(self):
        current = self.head
        while current:
            print(current.getValue())
            current = current.getNext()

#implementation
e1 = Element("cat")
e2 = Element("dog")
e3 = Element('monkey')
animals = LinkedList()
animals.append(e1)
animals.append(e2)
animals.append(e3)

animals.printList()


