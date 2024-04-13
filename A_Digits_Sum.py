t = int(input())
for i in range(t):
    n = int(input())
    m = str(n)
    if m[-1] == "9":
        print(n // 10 + 1)
    else:
        print(n // 10)
