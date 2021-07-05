class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # in- order
    def InorderPrintTree(self):
        if self.left:
            self.left.InorderPrintTree()
        print(self.data, end=" ")
        if self.right:
            self.right.InorderPrintTree()

    # post-order
    def PreorderPrintTree(self):
        print(self.data, end=" ")
        if self.left:
            self.left.PreorderPrintTree()
        if self.right:
            self.right.PreorderPrintTree()

    c = []

    def PostorderPrintTree(self):
        # self.c += 1
        # print(self.data,end=" ")
        if self.left:
            self.left.PostorderPrintTree()
        if self.right:
            self.right.PostorderPrintTree()
        self.c.append(self.data)
        print(self.data, end=" ")


def FindMinimumValue(node):
    if node == None:
        print("No node exist.")
    current = node
    while current.left != None:
        current = current.left
    return current.data


# recursive way
def SizeOfTree(node):
    if node == None:
        return 0
    else:
        return SizeOfTree(node.left) + 1 + SizeOfTree(node.right)


root = Node(1)
root.insert(2)
root.insert(5)
root.insert(6)
root.insert(3)
root.insert(4)
# root.insert(42)
print("Orginal Tree ", 1, 2, 5, 6, 3, 4)
print("In order: ")
root.InorderPrintTree()
print("\nPre order: ")
root.PreorderPrintTree()
print("\nPost order: ")
root.PostorderPrintTree()
print("\nMinimum value of BST: ")
print(FindMinimumValue(root))
print("Size of tree: ")
print(SizeOfTree(root))
print(len(root.c))
