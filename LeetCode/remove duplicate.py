def removeDuplicates(nums):
    # index = 0
    # dup_value = None
    # for i in nums:
    #     if dup_value != i:
    #         index += 1
    #         dup_value = i
    # return index
    return len(set(nums))


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
rd = removeDuplicates(nums)
print(rd)
