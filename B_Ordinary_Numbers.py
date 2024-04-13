t = int(input())
for i in range(t):
    n = int(input())
    ma = 9 * len(str(n))
    ans = ma - (9 - (n // 10 ** (len(str(n)) - 1)))
    string_version = str(n)
    start = string_version[0]
    compr = start * len(str(n))
    if int(string_version) < int(compr):
        print(ans - 1)
    else:
        print(ans)
