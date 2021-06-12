from sortLinkList import Node, LinkList


def remove_duplicate_unsorted_link_list(head):
    temp = head
    prev = None
    duplicate = []
    while temp:
        if temp.data not in duplicate:
            duplicate.append(temp.data)
            prev = temp
        else:
            prev.next = temp.next
        temp = temp.next
    return head


linklist = LinkList()
print("create link list")
head = linklist.create_link([1, 5, 6, 5, 6])
print(linklist.show_link_list(head))
print("Print after remove duplicate: ")
new_head = remove_duplicate_unsorted_link_list(head)
print(linklist.show_link_list(new_head))
