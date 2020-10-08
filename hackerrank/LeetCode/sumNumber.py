class Solution:
    def TwoSum(self,arr:List[int], target) -> List[List[int]]:

        for i in range(len(arr)):
            m = i + 1
            for k in arr[m:]:
                if arr[i] + k == target:
                    return i, m
                m += 1


arr = list(map(float, input().split()))
target = int(input())
print(list(TwoSum(arr, target)))
