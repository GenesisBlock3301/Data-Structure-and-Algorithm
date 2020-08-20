n1,n2,n3 = list(map(int,input().split()))
stack1 = [int(x) for x in input().split()][:n1]
stack2 = [int(x) for x in input().split()][:n2]
stack3 = [int(x) for x in  input().split()][:n3]

s1 = [*stack1[::-1]]
# print(s1)
s2 = [*stack2[::-1]]
s3 = [*stack3[::-1]]
# # print(stack1,s1)
for i in range(1,len(s1)):
    s1[i],s1[i-1] = s1[i]+s1[i-1],s1[i-1]

for i in range(1,len(s2)):
    s2[i],s2[i-1] = s2[i]+s2[i-1],s2[i-1]

for i in range(1,len(s3)):
    s3[i],s3[i-1] = s3[i]+s3[i-1],s3[i-1]

# print(s1,s2,s3)

arr1 = [*s1[::-1]]
arr2 = [*s2[::-1]]
arr3 = [*s3[::-1]]
flag = True
if len(arr1) <= len(arr2) and len(arr1) <= len(arr3):
    for i in arr1:
        if i in arr2 and i in arr3:
            print(i)
        else:
            flag = False
elif len(arr2) <= len(arr1) and len(arr2) <= len(arr3):
    for i in arr2:
        if i in arr1 and i in arr3:
            print(i)
        else:
            flag = False
elif len(arr3) <= len(arr2) and len(arr3) <= len(arr1):
    for i in arr3:
        if i in arr1 and i in arr2:
            print(i)
        else:
            flag = False
if flag == False:
    print(0)




