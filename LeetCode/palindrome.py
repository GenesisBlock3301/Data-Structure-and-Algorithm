
def isPalindrome(x):
    if x < 0:
        return False
    tem = str(x)[::-1]
    if str(x) == tem:
        return True
    return False
n = -121
print(isPalindrome(n))

#without string
def isPalindromeInt(x):
    if x < 0:
        return False
    n = x
    rev = 0
    while x > 0:
        rem = x%10
        x = x//10
        rev = rev*10+rem
    return rev == n
n = 121
print(isPalindromeInt(n))