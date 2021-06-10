# s = [1,2,1,3,2]
# m = 2
# # print(s[0:1])
# for i in range(len(s)-m):
#     print(s[i:m])
#     m+=1

n = int(input())
arr = [int(x) for x in input().split()][:n]
d, m = list(map(int, input().split()))
lenght = len(arr)
c = 0
if m == 1:
    if arr[0] == d:
        c+= 1
        print(c)
    else:
        print(c)

else:
    for i in range((lenght - m)+1):
        if sum(arr[i:i+m]) == d:
            c+=1
    print(c)
