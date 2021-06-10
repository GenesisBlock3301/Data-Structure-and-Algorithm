def plusOne(digits):
    ans = "".join([str(x) for x in digits])
    ans = int(ans) + 1
    return [int(x) for x in str(ans)]


print(plusOne([9, 9]))
