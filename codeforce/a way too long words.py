# n = "pneumonoultramicroscopicsilicovolcanoconiosis"
# print(len(n))

n = int(input())
for i in range(n):
    st = input()
    if len(st) > 10:
        print(st[0] + str(len(st) - 2) + st[-1])
    else:
        print(st)