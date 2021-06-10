def matche(a, b):
    if (a == "{" and b == "}") or (a == "(" and b == ")") or (a == "[" and b == "]"):
        return True
    else:
        return False

def isBalanced(s):
    mystack = []
    p = "NO"
    for i in s:
        if i in ["[", "{", "("]:
            mystack.append(i)
        else:
            if len(mystack) == 0:
                return "NO"
            else:
                b = mystack.pop()
            if matche(b, i):
                p = "YES"
            else:
                return "NO"
    if len(mystack) == 0:
        return p
    else:
        return "NO"

n = int(input())
for _ in range(n):
    print(isBalanced(input()))