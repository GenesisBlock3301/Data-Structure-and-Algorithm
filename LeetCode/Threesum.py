def threeSum(nums):
    n = len(nums)
    nums.sort()
    arr = []
    for i in range(n - 2):
        k = 0 - nums[i]
        l, h = i + 1, n - 1

        while l < h:
            if nums[l] + nums[h] < k:
                l += 1
            elif nums[l] + nums[h] > k:
                h -= 1
            else:
                if [nums[i], nums[l], nums[h]] not in arr:
                    arr.append([nums[i], nums[l], nums[h]])
                l += 1
                h -= 1
    return arr


print(threeSum([-1, 0, 1, 2, -1, -4]))
