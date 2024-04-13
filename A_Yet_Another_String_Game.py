t = int(input())
for i in range(t):
    st = input()
    st2 = ""
    for val in range(len(st)):
        if val % 2 == 0:
            if st[val] != "a":
                st2 += "a"
            else:
                st2 += "b"
        else:
            if st[val] != "z":
                st2 += "z"
            else:
                st2 += "y"
    print(st2)
