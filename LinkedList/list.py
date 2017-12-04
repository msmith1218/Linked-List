from node import node

class list(object):
    def __init__(self, head = None, count = 0):
        self.head = head
        self.count = count

    def insert(self, num):

        newNode = node(num)

        if self.count > 0:
            newNode.set_next(self.head)
            self.head.set_previous(newNode)
            self.head = newNode
            self.count += 1
        else:
            self.head = newNode
            self.count += 1


    def getValueAt(self, num):
        this = self.head
        if self.count < num:
            raise ValueError("number outside of list size")

        theCounter = 0
        while theCounter < num:
            this = this.get_next()
            theCounter += 1

        return this.get_data()

    def popValueAt(self, num):
        current = self.head
        if self.count < num:
            raise ValueError("number outside of list size")
        counter = 0
        while counter < num:
            current = current.get_next()
            counter += 1


        theNum = current.get_data()
        list.deleteValueAt()
        return theNum


    def size(self):
        return self.count

    def traverse(self):
        pass

    def traversePrint(self):
        c = 0
        print ("The contents of the linked list are: ")
        print ("")
        while c < list.size(self):
            value = list.getValueAt(self, c)
            print (value)
            print ("")
            c += 1


    def search(self, data):
        this = self.head
        isFound = False
        while this and isFound is False:
            if this.get_data() == data:
                isFound = True
            else:
                this = this.get_next()
        if this is None:
            raise ValueError("Data not in list")
        return this


    def delete(self, data):
        this = self.head
        prev = None
        found = False
        while this and found is False:
            if this.get_data() == data:
                found = True
            else:
                prev = this
                this = this.get_next()
        if this is None:
            raise ValueError("Data not in list")
        if prev is None:
            self.head = this.get_next()
        else:
            prev.set_next(this.get_next())


        self.count -= 1



