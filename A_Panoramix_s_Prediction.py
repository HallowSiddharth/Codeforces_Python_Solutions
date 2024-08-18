n, m = list(map(int, input().rstrip().split()))
ans = "NO"
for i in range(n + 1, m + 1):
    # doing a prime check for every i
    prime_status = True
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            prime_status = False
    # we only need the nearest prime number
    if prime_status:
        if m == i:
            ans = "YES"
        break

print(ans)
