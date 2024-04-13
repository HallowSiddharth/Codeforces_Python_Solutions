t=int(input())
for i in range(t):
    n=input()
    m=1
    for i in range(1,123456790):
        s=sum([int(j) for j in str(i)])
        if s==n:
            print(i)
            break
