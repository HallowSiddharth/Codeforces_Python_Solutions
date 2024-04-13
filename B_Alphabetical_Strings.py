t = int(input())
for i in range(t):
    st = input()
    lst = [value for value in st]
    length = len(st)
    start = length
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    while lst != []:
        if lst[0] == alphabets[start - 1]:
            lst.pop(0)
            start -= 1
        elif lst[-1] == alphabets[start - 1]:
            lst.pop(-1)
            start -= 1
        else:
            break
    if lst == []:
        print("YES")
    else:
        print("NO")
