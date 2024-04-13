t = int(input())
for i in range(t):
    ans = "NO"
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    for el in lst:
        if int(el**0.5) != el**0.5:
            ans = "YES"
    print(ans)
