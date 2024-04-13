t=int(input())
for i in range(t):
    a,b=list(map(int,input().rstrip().split()))
    if b==1:
        print("NO")

    else:
        print("YES")
        print(a,a*b,a+(a*b))

            