st1 = input()
st2 = input()

ans = ""

for i in range(len(st1)):
    if st1[i] == st2[i]:
        ans += "0"
    else:
        ans += "1"

print(ans)
