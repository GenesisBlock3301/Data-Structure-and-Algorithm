n = int(input())
arr = []
for i in range(n):
    arr.append(input())
arr1 = sorted(arr)
print(arr1)
a = sorted(arr1,key=len)
print(a)
# print("\n".join(a))
