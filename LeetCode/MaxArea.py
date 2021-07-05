def maxArea(height) -> int:
    i, j = 0, len(height) - 1
    mx = 0
    while i < j:
        if height[i] < height[j]:
            d = min(height[i], height[j])
            mx = max(mx, (j - i) * d)
            i += 1
        else:
            d = min(height[i], height[j])
            mx = max(mx, (j - i) * d)
            j -= 1
    return mx


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
