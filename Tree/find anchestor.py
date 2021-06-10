class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def maxDeptNode(node):

    if node == None:
        return 0
    else:
        # print(node.left,node.right)
        lDepth = maxDeptNode(node.left)
        print("L",lDepth)
        rDepth = maxDeptNode(node.right)
        print("R",rDepth)
        if lDepth > rDepth:
            print('Ll1',lDepth,rDepth)
            print("-------")
            return lDepth+1
        else:
            print('RR2', lDepth, rDepth)
            print("-------")
            return rDepth+1

root = Node(27)
root.left = Node(14)
root.right = Node(35)
root.left.left = Node(10)
root.left.right = Node(19)
root.right.left = Node(31)
root.right.right = Node(42)
root.left.left.left = Node(5)
root.left.left.right = Node(11)
print(maxDeptNode(root))