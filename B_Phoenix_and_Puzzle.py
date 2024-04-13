t = int(input())
for i in range(t):
    n = int(input())
    ans = "NO"
    if n % 2 == 0:
        a = (n / 2) ** 0.5 == int((n / 2) ** 0.5)
        b = (n / 4) ** 0.5 == int((n / 4) ** 0.5)
        if a or b :
            ans = "YES"
    print(ans)
