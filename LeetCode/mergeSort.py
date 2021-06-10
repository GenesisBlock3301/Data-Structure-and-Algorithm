def merge(nums1, m, nums2, n):
    nums1 = nums1[:m]
    nums2 = nums2[:n]
    new_list = []
    len_a, len_b = len(nums1), len(nums2)
    index_a, index_b = 0, 0
    while index_a < len_a and index_b < len(nums2):
        if nums1[index_a] < nums2[index_b]:
            new_list.append(nums1[index_a])
            index_a += 1
        else:
            new_list.append(nums2[index_b])
            index_b += 1
    if index_a < len(nums1):
        new_list.extend(nums1[index_a:])
    elif index_b < len(nums2):
        new_list.extend(nums2[index_b:])

    return new_list


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
a = merge(nums1, m, nums2, n)
print(a)
