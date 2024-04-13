import math

t = int(input())
for i in range(t):
    nt = int(input())
    n = math.ceil(math.sqrt(nt))
    # print("N", n)
    maxv = n**2
    if maxv - nt < n:
        row = n
        column = maxv - nt + 1
    else:
        d = n**2 - n
        row = n - (d + 1 - nt)
        column = n
    print(row, column)
