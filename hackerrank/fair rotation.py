def fairRot(arr):
    count = 0
    if sum(arr)%2 != 0:
        return "NO"

    for i in range(0,len(arr)):
        if arr[i]%2 != 0:
            arr[i] = arr[i]+1
            arr[i+1] = arr[i+1]+1
            count += 2
    return count


n = int(input())
arr = [int(x) for x in input().split()][:n]
print(fairRot(arr))