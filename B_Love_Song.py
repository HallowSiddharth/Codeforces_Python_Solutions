n, q = list(map(int, input().rstrip().split()))
st = input()
d = {}
alphabets = "abcdefghijklmnopqrstuvwxyz"
alpha = {}

for i in range(26):
    alpha[alphabets[i]] = i + 1

d[1] = alpha[st[0]]

for i in range(1, len(st)):
    d[i + 1] = d[i] + alpha[st[i]]

for _ in range(q):
    l, r = list(map(int, input().rstrip().split()))
    # print(d[r])
    if l == 1:
        print(d[r])
    else:
        print(d[r] - (d[l - 1]))
