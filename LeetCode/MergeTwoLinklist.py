class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None


    def insert_first(self,item):
        newNode = ListNode(item)
        newNode.next = self.head
        self.head = newNode

    def insert_last(self,item):
        newNode = ListNode(item)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode



    def showLinkList(self):
        temp = self.head
        while temp != None:
            print(temp.val)
            temp = temp.next


list = LinkList()
list.insert_first(3)
list.insert_first(6)
list.showLinkList()
print("Insert last: ")

