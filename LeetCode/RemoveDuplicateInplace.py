def removeDuplicates(nums) -> int:
    i = 0
    tem = []
    k = len(nums)
    while i < len(nums):
        # print(nums[i])
        if nums[i] in tem:
            nums[i] = "_"
            # print("if", nums, i)
        else:
            tem.append(nums[i])
            if i > 0:
                if "_" in nums:
                    index = nums.index("_")
                    nums[i], nums[index] = nums[index], nums[i]
            # print("else:", nums, i)

        i += 1

    while "_" in nums:
        nums.remove("_")

    return nums


# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1, 1, 2]
nums = [1, 1, 2, 3]
print(removeDuplicates(nums))
