def removeDuplicates(nums) -> int:
    for i in nums:
        while nums.count(i) > 2:
            nums.remove(i)
    return len(nums)

nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))
