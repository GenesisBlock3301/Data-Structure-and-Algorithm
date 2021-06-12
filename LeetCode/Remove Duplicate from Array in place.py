def removeDuplicates(nums) -> int:
    dup = []
    i = 0
    n = len(nums)
    while nums and i != len(nums):
        print(i)
        if nums[i] not in dup:
            dup.append(nums[i])
            i += 1
        else:
            nums[i] = nums[i + 1]
            nums[n-1] = 0




nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
