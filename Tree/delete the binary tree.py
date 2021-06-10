class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def Rec_DeleteBinaryTree(root):
    if root == None:
        return

    Rec_DeleteBinaryTree(root.left)
    Rec_DeleteBinaryTree(root.right)

    del root
    root = None
    return root

def Iter_DeletionBinaryTree(root):
    if root == None:
        return

    queue = []
    queue.append(root)

    while queue != None:

        node = queue[0]
        queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        del node

    root = None
    return root

def showBanrytree(root):
    if root.left:
        showBanrytree(root.left)
    if root.right:
        showBanrytree(root.right)
    print(root.data,end=" ")


root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)
print("Before Deletion Binary tree:")
showBanrytree(root)
print("\nDelete binary tree:",Rec_DeleteBinaryTree(root))
print("\n IternDelete binary tree:",Iter_DeletionBinaryTree(root))
print("After deletion binary Tree:")
if root:
    showBanrytree(root)
else:
    print("Tree is emty.")