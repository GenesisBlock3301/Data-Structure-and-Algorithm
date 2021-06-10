def addBinary(a: str, b: str) -> str:

    sum1 = 0
    for i, v in enumerate(a[::-1]):
        sum1 += (2 ** i) * int(v)
    sum2 = 0
    for i, v in enumerate(b[::-1]):
        sum2 += (2 ** i) * int(v)
    val = sum1 + sum2
    store = ''
    while val > 0:
        rem = val % 2
        val = val // 2
        store += str(rem)
    if val == '':
        return '0'

    return store[::-1]


a = "0"
b = "0"
print(addBinary(a, b))
