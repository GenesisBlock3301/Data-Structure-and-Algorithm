
# def invalid_bracket(str):
#     stack, bracket = [],{"(": ")"}
#     count = 0
#     arr = list(str)
#     for p in range(len(arr)):
#         if arr[p] in bracket:
#             stack.append(arr[p])
#         elif len(stack) == 0 or bracket[stack.pop()] != arr[p]:
#             stack = [arr[p]]+stack
#             count += 1
#             print("Index",arr.index(arr[p]))
#
#     if len(stack) > 0:
#         return len(stack)
#     else:
#         return count



def invalid_bracket(str):
    stack, bracket = [],{"(": ")"}
    count = 0
    arr = list(str)
    index = []
    for p in range(len(arr)):
        if arr[p] in bracket:
            stack.append(arr[p])
            index.append(p)
        elif len(stack) == 0 or bracket[stack.pop()] != arr[p]:
            stack = [arr[p]]+stack
            count += 1
            index.append(p)
    print(index)
    if len(stack) > 0:
        return len(stack)
    else:
        return count

# n = int(input())
st = "(()))("
print(invalid_bracket(st))



