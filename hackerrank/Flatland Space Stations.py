# import time
# start = time.time()
n, m = list(map(int, input().split()))
arr = [int(x) for x in input().split()][:m]
max_distance = max(arr[0],n-arr[-1]-1)
for i in range(1,m):
    d = arr[i] - arr[i-1]
    max_distance = max(d//2,max_distance)
print(max_distance)
# end = time.time()
# print("Total time:",end-start)