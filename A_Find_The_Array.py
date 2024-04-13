    import math

    t = int(input())
    for i in range(t):
        n = int(input())
        ct = 0
        temp = 0
        j = 1
        while n > temp:
            ct += 1
            temp += j
            j += 2
        print(ct)
