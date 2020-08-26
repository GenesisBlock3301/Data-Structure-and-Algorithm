t = int(input())
for k in range(t):
    n = int(input())
    a = int(input())
    b = int(input())
    s = set()
    for i in range(n):
        value = a * i + (n - 1 - i) * b
        s.add(value)
    values = sorted(s)
    for x in values:
        print(x, end=' ')
