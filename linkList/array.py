arr = [4,3,1,2]
# codeforce = []
# c=0
# for i in range(len(arr)):
#    if arr:
#        min_val = min(arr)
#        codeforce.append(min_val)
#        arr.remove(min_val)
#        # print(arr)
#        c+=1
#    else:
#        break
# print(codeforce,c)
# print(codeforce.index(min(codeforce)))

c = 0
for i in range(len(arr)):
    print(arr[i],min(arr[i+1:]))
    if arr[i] > min(arr[i+1:]):
        # print(arr)
        # print(i,arr.index(min(arr[i+1:])),"IN")
        arr[i],arr[arr.index(min(arr[i+1:]))] = arr[arr.index(min(arr[i+1:]))],arr[i]
        print(arr)
        # break



# arr[0],arr[2] = arr[2],arr[0]
# print(arr)