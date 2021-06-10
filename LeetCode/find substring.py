def findSub(s, sub):
    index = 0
    for i in s:
        if i == sub[0]:
            temp = s[index:index + len(sub)]
            if temp == sub:
                return index
        index += 1
    return -1


index = findSub("dedicate", 'cat')
print(index)
