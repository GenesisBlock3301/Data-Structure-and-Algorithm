def RomanToInteger(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    ans = 0
    while i < len(s):
        if s[i:i + 2] in roman:
            ans += roman[s[i:i + 2]]
            i += 2
        else:
            ans += roman[s[i]]
            i += 1
    return ans


print(RomanToInteger('III'))
