class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_last(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def insert_after_item(self,x,data):
        new_node  = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                if temp.data == x:
                    break
                temp.next

            if temp == None:
                print("Item not found")
            else:
                new_node.next = temp.next
                temp.next = new_node


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

n = int(input("How many item make operation: "))

llist = LinkList()
for i in range(n):
    item = int(input())
    # llist.insert_at_start(item)
    llist.insert_at_last(item)

# llist.insert_after_item(int(input("Input your target value: ")),int(input("Data: ")))
llist.print_list()