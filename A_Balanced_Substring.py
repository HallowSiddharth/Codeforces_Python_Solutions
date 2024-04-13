t = int(input())
for i in range(t):
    n = int(input())
    st = input()
    ans = False
    for char in range(len(st) - 1):
        if (st[char] == "a" and st[char + 1] == "b") or (
            st[char] == "b" and st[char + 1] == "a"
        ):
            ans = [char, char + 1]
            break
    if ans:
        print(ans[0] + 1, ans[1] + 1)
    else:
        print(-1, -1)
