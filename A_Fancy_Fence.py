t=int(input())
for i in range(t):
    a=int(input())
    sides= 360/(180-a)
    if int(sides)==sides:
        print("YES")
    else:
        print("NO")