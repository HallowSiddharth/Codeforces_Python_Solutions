n = int(input())

# first half
lst = []
for i in range(n + 1):
    st = " " * (n - i) * 2
    for j in range(i + 1):
        st += str(j) + " "

    for k in range(i - 1, -1, -1):
        st += str(k) + " "

    lst.append(st[:-1])

# 2nd half, everything repeats in reverse, so we just add the same
for i in lst[-2::-1]:
    lst.append(i)

for i in lst:
    print(i)
