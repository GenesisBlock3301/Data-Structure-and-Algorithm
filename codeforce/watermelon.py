def findEven(n):
    if n <=3:
        return 1,1
    else:
        arr = [int(x) for x in list(range(1, n - 1))]
        for i in range(1, n - 1):
            for k in arr:
                if i + k == n:
                    return (i, k)

if __name__ == "__main__":
    n = int(input())#
    tup = findEven(n)
    if tup[0]%2 == 0 and tup[1]%2==0:
        print("YES")
    else:
        print("NO")