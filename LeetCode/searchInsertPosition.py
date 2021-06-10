def searchInsert(nums, target):
    b = [target]
    new_list = []
    len_a, len_b = len(nums), len(b)
    index_a, index_b = 0, 0
    while index_a < len(nums) and index_b < len(b):
        if nums[index_a] < b[index_b]:
            new_list.append(nums[index_a])
            index_a += 1
        else:
            new_list.append(b[index_b])
            index_b += 1
    if index_a < len(nums):
        new_list.extend(nums[index_a:])
    elif index_b < len(b):
        new_list.extend(b[index_b:])

    return new_list.index(target)


nums = [1, 3, 5, 6]
target = 0
a = searchInsert(nums, target)
print(a)
