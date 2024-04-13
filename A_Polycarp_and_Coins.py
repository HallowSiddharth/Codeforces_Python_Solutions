t=int(input())
for i in range(t):
    n=int(input())
    r=n%3
    if r==0:
        print(n//3,n//3)
    elif r==1:
        print((n//3)+1,n//3)
    elif r==2:
        print(n//3,n//3+1)