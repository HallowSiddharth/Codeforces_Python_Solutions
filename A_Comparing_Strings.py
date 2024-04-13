s1 = list(input())
s2 = list(input())
ct = 0
# non matching elements 1 and 2

st1 = list(s1)
st2 = list(s2)
ans = "NO"
st1.sort()
st2.sort()
if st1 == st2:
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            ct += 1

    if ct == 2:
        ans = "YES"

print(ans)
