n,k = list(map(int,input().split()))
arr = [int(x) for x in input().split()]

page = 1
sp = 0
for c in range(0,n):
    problems = arr[c]
    for i in range(1,problems):
        if i == page:
            sp+=1
        if i%k == 0 or i == k:
            page+=1
print(sp)