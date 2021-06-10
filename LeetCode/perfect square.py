def isPerfectSquare(num: int) -> bool:
    if num == 1:
        return True
    left = 0
    right = num
    while left + 1 < right:
        mid = (left + right) // 2
        if mid * mid == num:
            return True
        if mid * mid < num:
            left = mid
        elif mid * mid > num:
            right = mid
    return False


# ans = (num ** 0.5) * 10 % 10
# if ans == 0:
#     return True
# return False


print(isPerfectSquare(3))
