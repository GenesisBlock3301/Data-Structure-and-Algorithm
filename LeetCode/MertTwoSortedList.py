def merge(nums1, m, nums2, n):
    # if n == 0:
    #     return nums1
    # if m == 0:
    #     nums1.c
    for i in range(m,len(nums1)):
        nums1.pop()
    for i in nums2:
        nums1.append(i)
    nums1.sort()
    return nums1


nums1 = [4, 0, 0, 0, 0, 0]
m = 1
nums2 = [1, 2, 3, 5, 6]
n = 5

print(merge(nums1, m, nums2, n))
