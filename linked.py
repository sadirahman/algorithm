class node (object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def remove(self, data, previousNode):
        if self.data == data:
            previousNode.nextNode = self.nextNode
            del self.data
            del self.nextNode
        else:
            if self.nextNode is not None:
                self.nextNode.removr(data, self)
class linked:

    def __init__(self):
        self.head = None
        self.counter= 0

    def traverseList(self):
        actualNode =self.head

        while actualNode is not node:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode

    def insertStart(self, data):
        self.counter +=1
        newNode = node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head =newNode

    def size(self):
        return self.counter

    def insertEnd(self, data):

        if self.head is None:
            self.insertStart(data)
            return

        self.counter +=1

        newNode = node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

            actualNode.nextNode = newNode

    def remove (self, data):
        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data, self.head)
    
my = linked()
my.insertStart(2)
my.insertEnd(3)
my.insertEnd(4)
my.traverseList()

