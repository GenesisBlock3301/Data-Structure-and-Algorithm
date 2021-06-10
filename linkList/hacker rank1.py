
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(head):
    # temp = head
    # while temp:
    #     print(temp.data)
    #     temp = temp.next
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next

def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    if not head:
        head = new_node
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    return head
    return head
if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)