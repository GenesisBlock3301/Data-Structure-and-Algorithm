def find_min(a, n):
    if n == 1:
        return a[0]
    return min(a[n - 1], find_min(a, n - 1))


array = [1, 2, 3, -1]
print(find_min(array, len(array)))
