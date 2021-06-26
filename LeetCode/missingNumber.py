def missingNumber(nums) -> int:
    n = len(nums)
    s1 = 0
    s2 = sum(nums)
    for i in range(n+1):
        s1 += i
    return s1-s2


nums = [0,1]
print(missingNumber(nums))
