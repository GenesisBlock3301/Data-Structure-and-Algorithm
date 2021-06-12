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

    def remove_duplicate(self, head):
        tem = head
        while tem.next is not None:
            if tem.data == tem.next.data:
                new = tem.next.next
                tem.next = new
            else:
                tem = tem.next

        return head

    def show_link_list(self, head):
        if head is None:
            return head
        tem = head
        while tem.next is not None:
            print(tem.data)
            tem = tem.next
        print(tem.data)
        return



if __name__ == "__main__":
    print("Pass list item for creating link list:")
    link_list = LinkList()
    head = link_list.create_link(None)
    print("Show unique value")
    print(link_list.remove_duplicate(head))
    print("Show link list: ")
    print(link_list.show_link_list(head))
