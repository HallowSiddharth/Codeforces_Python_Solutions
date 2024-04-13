t=int(input())
for i in range(t):
    n=int(input())
    if n==1:
        print(0)
    elif n==2:
        print(-1)
    elif n==3:
        print(2)
    else:
        s=0
        while True:
            if n%6==0:
                n=n//6
                s+=1
            elif n%3==0:
                n=n*2
                s+=1
            else:
                break
        if n==1:
            print(s)
        else:
            print(-1)