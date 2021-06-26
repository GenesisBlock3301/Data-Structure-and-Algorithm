def findDuplicate(nums) -> int:
    c = 0
    tem = [False]*len(nums)
    for i in nums:
        if tem[i] is True:
            return i
        else:
            tem[i] = True


nums = [3, 1, 3, 4, 2]
print(findDuplicate(nums))