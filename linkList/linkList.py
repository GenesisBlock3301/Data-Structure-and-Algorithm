class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None


def insert(head, data):
    node = Node(data)
    if not head:
        head = node
    else:
        node.next = head.next
        head.next = node
    return head


def printLinkedList(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next


def count_link_list(head):
    temp = head
    c = 0
    while temp:
        c += 1
        temp = temp.next
    return c


if __name__ == '__main__':
    llist_count = int(input())

    llist = LinkList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insert(llist.head, llist_item)
        llist.head = llist_head

    printLinkedList(llist.head)
    print("Number of link list: ", count_link_list(llist_head))
