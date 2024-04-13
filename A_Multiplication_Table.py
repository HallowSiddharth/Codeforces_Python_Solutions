n, x = list(map(int, input().rstrip().split()))
ans = 0
factors = []

for i in range(1, n + 1):
    if x % i == 0:
        factors.append(i)

for i in factors:
    if x / i in factors:
        ans += 1

print(ans)
# if x**0.5 == int(x**0.5):
#     print((ans - 1) * 2 + 1)
# else:
#     print(ans * 2)
