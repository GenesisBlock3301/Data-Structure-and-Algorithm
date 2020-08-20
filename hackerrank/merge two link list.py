class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkListA:
    def __init__(self):
        self.head = None

    def insertNodeA(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
        return self.head

    def showLinkListA(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

class LinkListB:
    def __init__(self):
        self.head = None

    def insertNodeB(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def showLinkListB(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llist = LinkListA()
llist2 = LinkListB()
n = int(input("How many item you want to insert at last: "))
for i in range(n):
    data = int(input("Enter value for First Link List: "))
    llist.insertNodeA(data)
print("Show link list 1: ")
llist.showLinkListA()

print("----------------------------------------------")
for i in range(n):
    data = int(input("Enter value for Second Link List: "))
    llist2.insertNodeB(data)
print("Show second Link list: ")
llist2.showLinkListB()