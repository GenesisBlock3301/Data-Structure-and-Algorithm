arr = [1, 4, 5, 2, 6, 4, 3]


def bellow(arr):
    arr1 = []
    arr2 = []
    for i in arr:
        if i <= 4:
            arr1.append(str(i))
        else:
            arr2.append(str(i))
    print("List-1:", " ".join(arr1))
    print("List-2:", " ".join(arr2))

bellow(arr)

from math import ceil, floor


def median(arr):
    arr = sorted(arr)
    if len(arr) % 2 == 0:
        n = len(arr) / 2
        return (arr[ceil(n)] + arr[floor(n)]) / 2
    else:
        n = len(arr)/2
        # print(n)
        return arr[floor(n)]

def mean(arr):
    sum = 0
    for i in arr:
        sum+=i
    return sum/len(arr)

def mode(arr):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 1
    ans = sorted(dic.items(),key=lambda x:x[1])
    return ans[-1][0]

def swap(a,b):
    x = a
    a = b
    b = x
    return a,b
# n+nn+nnn
def sequence(n):
    sum = 0
    for i in range(1,4):
        sum+=int(str(n)*i)
    return sum
a = [1,2,3]
b = [4,5]
a,b = swap(a,b)
print("Swap: ",a,b)

arr = [1, 2, 3, 4,3, 5]
print("Median :",median(arr))
print("Mean :",mean(arr))
print("Mode :",mode(arr))
print('SECUENCE',sequence(5))