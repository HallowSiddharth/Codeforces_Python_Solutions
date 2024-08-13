st = input()
lst = [i for i in st]
ans = ""
while lst != []:
    # .
    if lst[0] == ".":
        lst.pop(0)
        ans += "0"
    else:
        # -.
        if lst[1] == ".":
            lst.pop(0)
            lst.pop(0)
            ans += "1"
        # --
        else:
            lst.pop(0)
            lst.pop(0)
            ans += "2"

print(ans)
