def findErrorNums(nums) -> int:
    missing = None
    n = len(nums)+1
    tem = [False] * n
    print(tem)
    for i in nums:
        if tem[i] is True:
            missing = i
        else:
            tem[i] = True
        if missing is not None:
            break
    s = sum(list(range(1, len(nums) + 1)))
    set_sum = sum(nums) - missing
    return [missing, s - set_sum]


nums = [2,2]
print(findErrorNums(nums))
