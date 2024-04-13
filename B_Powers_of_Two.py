t = int(input())
lst = list(map(int, input().rstrip().split()))
d = {}
l = [1, 2]
i = l[-1]

while i < 10**9:
    i = i * 2
    l.append(i)

for i in lst:
    try:
        d[i] += 1
    except:
        d[i] = 1

ans = 0
# print(d)
for key in d:
    for p in l:
        if p / 2 == key:
            ans += int((d[key] * (d[key] - 1)))
            # print(key, key, int((d[key] * d[key] - 1)))
        else:
            try:
                ans += d[key] * d[p - key]
                # print(key, p - key)
            except:
                continue

print(ans // 2)
