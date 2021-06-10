import math


def merge(a, b):
    # print("inside merge", a, b)
    merged_list = []
    len_a, len_b = len(a), len(b)
    index_a, index_b = 0, 0
    while index_a < len_a and index_b < len_b:
        if a[index_a] < b[index_b]:
            merged_list.append(a[index_a])
            index_a += 1
        else:
            merged_list.append(b[index_b])
            index_b += 1
    if index_a < len_a:
        merged_list.extend(a[index_a:])
    elif index_b < len_b:
        merged_list.extend(b[index_b:])
    return merged_list


def merge_sort(L):
    # print(L)
    if len(L) <= 1:
        return L

    mid = len(L) // 2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    # print('Left', left, 'Right', right)
    return merge(left, right)


def max_score(array, m):
    l_p = math.ceil(len(array) / m)
    fist_part = array[:-l_p]
    last_part = array[-l_p:]
    # print(fist_part)
    # print(last_part)
    start = 0
    end = m
    s = 0
    for i in range(1, m + 1):
        s += i * (sum(fist_part[start:end])%10)%10
        start = end
        end += m
    s += m * (sum(last_part))
    return s


n, m = [int(x) for x in input().split()][:2]
lis = [int(x) for x in input().split()]
if n == m or m == 1 or n == 1:
    print(sum(lis))
else:
    array = merge_sort(lis)
    print(max_score(array, m))
