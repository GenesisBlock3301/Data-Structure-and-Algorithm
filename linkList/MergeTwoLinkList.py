class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def create_link(self, elements):
        self.head = Node(elements[0])
        for element in elements[1:]:
            tem = self.head
            while tem.next is not None:
                tem = tem.next
            tem.next = Node(element)
        return self.head

    def merge_two(self, head1, head2):
        tem = head1
        while tem.next:
            tem = tem.next
        tem.next = head2

    def show_link_list(self, head):
        if head is None:
            return head
        tem = head
        while tem.next is not None:
            print(tem.data)
            tem = tem.next
        print(tem.data)


print("Pass list item for creating link list:")
link_list = LinkList()
head1 = link_list.create_link([1, 2, 4])
head2 = link_list.create_link([1, 3, 4])
link_list.merge_two(head1, head2)
print("Show link list: ")
print(link_list.show_link_list(head1))
