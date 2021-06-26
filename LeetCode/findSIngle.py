def singleNumber(nums) -> int:
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    l = [x for x in dic if dic[x] == 1]
    return l[0]


nums = [2, 2, 1]
print(singleNumber(nums))
