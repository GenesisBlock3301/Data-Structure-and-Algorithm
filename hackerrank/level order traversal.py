class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

#
# def levelOrder(root):
#     temp = root
#     stack = []
#     stack.append(temp.info)
#     while stack:
#         t = stack.pop(0)
#         print(t)
#         if temp.left:
#             stack.append(temp.info)
#         if temp.right:
#             stack.append(temp.info)
def levelOrder(root):
    qroot = []
    print(root.info,end=' ')
    if root.left:
        qroot.append(root.left)
    if root.right:
        qroot.append(root.right)

    while(qroot):
        tmp = qroot[0]
        if tmp.left:
            qroot.append(tmp.left)
        if tmp.right:
            qroot.append(tmp.right)
        print (tmp.info,end=' ')
        qroot.pop(0)



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))
print(arr)

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)