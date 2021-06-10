n = -2147483648

def revserInteger(x):
    tem = abs(x)
    if x < 0:
        ans = -int(str(tem)[::-1])
    else:
        ans = int(str(tem)[::-1])
    if ans > -12**31 and ans < (2**31)-1:
        return ans
    else:
        return 0


print(revserInteger(n))
