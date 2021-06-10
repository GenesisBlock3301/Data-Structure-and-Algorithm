def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1
    for i in range(1, x):
        if i * i == x:
            return i
        elif i * i > x:
            left = i - 1
            right = i
            while left <= right:
                mid = (left + right) / 2
                if int(mid * mid) == x:
                    return int(mid)
                if mid * mid < x:
                    left = mid
                elif mid * mid > x:
                    right = mid


x = 3
print(mySqrt(x))
