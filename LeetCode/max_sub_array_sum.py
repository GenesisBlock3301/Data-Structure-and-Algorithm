# kaden's algorithm
def maxSubArray(nums):
    store_val = -2147483648
    iterator_val = 0
    for i in range(len(nums)):
        iterator_val += nums[i]
        store_val = max(store_val, iterator_val)
        if iterator_val < 0:
            iterator_val = 0
    return store_val


nums = [-1]
a = maxSubArray(nums)
print(a)
