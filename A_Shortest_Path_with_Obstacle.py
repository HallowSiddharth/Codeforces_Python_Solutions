t = int(input())
for i in range(t):
    mt = input()
    ax, ay = list(map(int, input().rstrip().split()))
    bx, by = list(map(int, input().rstrip().split()))
    fx, fy = list(map(int, input().rstrip().split()))
    if ax == bx and ay == by:
        print(0)
    elif ax == bx:
        if fx == bx:
            if fy > max(ay, by) or fy < min(ay, by):
                print(abs(ay - by))
            else:
                print(abs(ay - by) + 2)
        else:
            print(abs(ay - by))
    elif ay == by:
        if fy == by:
            if fx > max(ax, bx) or fx < min(ax, bx):
                print(abs(ax - bx))
            else:
                print(abs(ax - bx) + 2)
        else:
            print(abs(ax - bx))
    else:
        print(abs(ax - bx) + abs(ay - by))
