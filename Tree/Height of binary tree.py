class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return self.data

    def PreorderPrintTree(self):
        print(self.data,end=" ")
        if self.left:
            self.left.PreorderPrintTree()
        if self.right:
            self.right.PreorderPrintTree()

def recursive_height(root):
    if root == None:
        return 0
    return 1+max(recursive_height(root.left),recursive_height(root.right))

def iterative_height(root):
   if root is None:
       return 0
   height = -1
   queue= []
   queue.append(root)
   while(queue !=None):
       nodeCount = len(queue)
       if nodeCount == 0:
           return height
       height+=1

       while nodeCount > 0:
           node = queue[0]
           queue.pop(0)
           if node.left != None:
               queue.append(node.left)
           if node.right != None:
               queue.append(node.right)
           nodeCount -= 1
   return height

root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.left.left.left = Node(16)
root.left.left.right = Node(25)
# print("Print Tree:")
# root.PreorderPrintTree()
print("\nRecursive height: ",recursive_height(root))
print("Iterative height: ",iterative_height(root))