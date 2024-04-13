t=int(input())
for i in range(t):
    a,b,c=list(map(int,input().rstrip().split()))
    if a==b and b==c:
        if a%2==0:
            print("Yes")
        else:
            print('No')
    elif a==b or a==c or b==c:
        if a==b:
            if c%2==0:
                print("Yes")
            else:
                print("No")
        elif b==c:
            if a%2==0:
                print("Yes")
            else:
                print("No")
        if c==a:
            if b%2==0:
                print("Yes")
            else:
                print("No")

    else:
        l2=[a,b,c]
        l2.sort()
        if l2[2]==l2[0]+l2[1]:
            print("Yes")
        else:
            print("No")