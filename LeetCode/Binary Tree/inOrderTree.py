class Node:
    def __init__(self, vale):
        self.val = vale
        self.left = None
        self.right = None


def in_order(root):
    stack = []
    store = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            store.append(current.val)
            current = current.right
        else:
            break

    return store

def pre_order(root):
    stack = []
    store = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            store.append(current.val)
            current = current.right
        else:
            break

    return store


root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

print(in_order(root))