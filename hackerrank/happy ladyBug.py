def lady_bug(n, a):
    dic = dict()
    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for k in dic.items():
        if k[0] != "_" and k[1] == 1:
            return "NO"

    if a.count("_") == 0:
        for m in range(1, n - 1):
            if a[m] != a[m - 1] and a[m] != a[m + 1]:
                return "NO"

    return "YES"


n = int(input())
for i in range(n):
    l = int(input())
    a = input()
    print(lady_bug(l, a))
