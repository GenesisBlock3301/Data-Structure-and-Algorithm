def isHappy(n: int) -> bool:
    while  n > 1:
        while n >= 100:
            n = n // 10
        rem = n % 10
        # if n >= 100:
        #     n = n // 10
        n = (n // 10) ** 2 + rem ** 2
        # print(n)
        # n = sum(list(map(lambda x: x ** 2, [int(x) for x in list(str(n))])))
    return True if n == 1 else False


print(isHappy(2))
