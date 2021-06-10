def solve(n, lookup={}):
    if n < 0:
        return 0
    if n == 0:
        return 1

    if n not in lookup:
        lookup[n] = solve(n - 1) + solve(n - 3) + solve(n - 5)
    return lookup[n]


print(solve(3))
