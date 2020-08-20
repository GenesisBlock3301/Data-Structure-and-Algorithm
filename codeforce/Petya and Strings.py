st1 = input().lower()
st2 = input().lower()
if len(st1) == len(st2):
    if st1 == st2:
        print(0)
    elif st1 > st2:
        print(1)
    else:
        print(-1)