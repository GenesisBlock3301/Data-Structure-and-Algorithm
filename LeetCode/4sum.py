def threeSum(nums, target):
    n = len(nums)
    nums.sort()
    arr = []
    for i in range(n - 1):
        # print(i)
        for j in range(i + 1, n):
            # print(j)
            k = target - (nums[i] + nums[j])
            l, h = j + 1, n - 1

            while l < h:
                # print("while")
                if nums[l] + nums[h] < k:
                    l += 1
                elif nums[l] + nums[h] > k:
                    h -= 1
                else:
                    if [nums[i], nums[j], nums[l], nums[h]] not in arr:
                        arr.append([nums[i], nums[j], nums[l], nums[h]])
                        # print(arr)
                    l += 1
                    h -= 1
    return arr


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(threeSum(nums, target))
