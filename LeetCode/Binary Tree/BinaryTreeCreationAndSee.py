class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.value}"

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node


def create_node():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    nine.add_right(eight)
    three = Node(3)
    four = Node(4)
    eight.add_right(four)
    eight.add_left(three)

    return two


def pre_order(node):
    print(node)
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)


if __name__ == "__main__":
    root = create_node()
    pre_order(root)
