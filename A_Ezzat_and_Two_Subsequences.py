t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    ma = max(lst)
    lst.remove(ma)
    print(sum(lst)/len(lst) + ma)
