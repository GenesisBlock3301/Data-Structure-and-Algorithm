class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return self.data


def iter_PreOrder(root):
    if root == None:
        return

    stack = []
    stack.append(root)
    while len(stack) > 0:
        node = stack.pop()
        print(node.data,end=" ")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def iter_InOrder(root):
    arr = []
    stack = []
    stack.append(root)
    node = root.left
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
            # print("left",stack)
            # break
        else:
            node = stack.pop()
            print(node.data,end=" ")
            arr.append(node.data)
                # print('Right',stack)
            node = node.right

def iter_PostOrder(root):
    # node = root
    traverse_stack = []
    post_stack = []
    traverse_stack.append(root)

    while traverse_stack:
        node = traverse_stack.pop()
        post_stack.append(node)

        if node.left:
            traverse_stack.append(node.left)
        if node.right:
            traverse_stack.append(node.right)

    while post_stack:
        node = post_stack.pop()
        print(node.data,end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("PreOrder traversal Iterative Process: ")
iter_PreOrder(root)
print("\nInOrder traversal Iterative Process: ")
iter_InOrder(root)
print("\nPostOrder traversal Iterative process: ")
iter_PostOrder(root)