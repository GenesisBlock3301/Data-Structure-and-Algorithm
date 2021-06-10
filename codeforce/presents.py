n = int(input())
arr = [int(x) for x in input().split()][:n]
lis = [0]*n
for i in range(0,n):
    lis[arr[i]-1] = i+1
for i in lis:
    print(i)