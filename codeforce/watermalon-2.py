def findEven(n):
    return True if n % 2 == 0 and n > 2 else False


if __name__ == "__main__":
    n = int(input())  #
    tup = findEven(n)
    print("YES" if tup is True else "NO")
