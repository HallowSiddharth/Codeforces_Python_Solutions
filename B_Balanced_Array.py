t=int(input())
for i in range(t):
    n=int(input())
    if (n//2) %2 ==1:
        print("NO")
    else:
        print("YES")
        lst=[]
        for i in range(1,(n//2)+1):
            lst.append(str(2*i))
        for j in range(n//2-1):
            lst.append(str(2*j+1))
        lst.append(str((2*(j+1))+1 + ((n//2))))
        print(' '.join(lst))