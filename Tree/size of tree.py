class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


#recursive way
def size(node):
    if node is None:
        return 0
    else:
        return size(node.left)+1+size(node.right)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(11)
root.right.left = Node(44)
print("Size of array: ",size(root),it_size(root))