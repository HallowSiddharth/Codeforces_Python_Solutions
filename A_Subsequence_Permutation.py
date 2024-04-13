t = int(input())
for i in range(t):
    n = int(input())
    st = input()
    lst = [j for j in st]
    copy = list(lst)
    copy.sort()
    k = 0
    for val in range(n):
        if lst[val] != copy[val]:
            k += 1
    print(k)
