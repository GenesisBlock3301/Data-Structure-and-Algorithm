def longestCommonPrefix(strs) -> str:
    s = ''
    for i in strs[0]:
        s += i
        for j in strs[1:]:
            for k in j:
                if s != k:
                    return s[:-1]
    return s


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))