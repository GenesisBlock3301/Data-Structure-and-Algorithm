from queue import LifoQueue

stack = LifoQueue(maxsize = 3)

print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')
print("Full stack: ",stack.full())
print("Stack Size: ",stack.qsize())

print("Element pop from the stack: ")
print(stack.get())
print(stack.get())
print(stack.get())
print("Empty: ",stack.empty())