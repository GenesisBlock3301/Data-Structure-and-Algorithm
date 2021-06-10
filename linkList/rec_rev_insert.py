
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None


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


def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    if not head:
        head = new_node
    else:
        c = 0
        prev = None
        temp = head
        while c < position and temp:
            prev = temp
            temp = temp.next
            c+=1
        prev.next = new_node
        new_node.next = temp
    return head

def delete_specific_Item(head,item):
    temp = head
    prev = None
    remove = None
    if head.data == item:
        temp = head.next
        head = temp
        # print("Done",head.data)
        return head
    else:
        while temp:
            if temp.data == item:
                remove = temp.next
                break
            prev = temp
            temp = temp.next
        prev.next = remove
        return head
def delete_specific_position(head,position):
    temp = head
    prev = None
    remove = None
    c = 0
    if c == 0 and position == 0:
        temp = head.next
        head = temp
        # print("Done",head.data)
        return head
    else:
        while temp:
            if c == position:
                remove = temp.next
                break
            c+=1
            prev = temp
            temp = temp.next
        prev.next = remove
        return head


def insertNodeAtHead(head, data):
    new_node = SinglyLinkedListNode(data)
    if not head:
        head = new_node
    else:
        new_node.next = head
        head = new_node
    return head

def print_singly_linked_list(head):
    if head == None:
        print("There are no node  exists.")
    else:
        temp = head
        while temp:
            print(temp.data)
            temp = temp.next

def reverse_rec(head):
    temp = head
    if temp:
        reverse_rec(temp.next)
        print(temp.data)

def reverse(head):
    current = head
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    head = prev
    return head
if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head,llist_item)
        llist.head = llist_head

    # print(insertNodeAtPosition(llist.head,1,2))
    # print(insertNodeAtHead(llist.head,3999))
    print_singly_linked_list(llist.head)
    print("Reverse: ")
    ll1 = reverse(llist_head)
    print_singly_linked_list(ll1)
    # print("Print after delete: ")
    # llist_head1 = delete_specific_position(llist_head,int(input("enter your remove position: ")))
    # print_singly_linked_list(llist_head1)
