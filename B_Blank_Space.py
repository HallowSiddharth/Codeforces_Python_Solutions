t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().rstrip().split()))
    l_zero=0
    temp=0
    try:
        for i in range(n):
            if arr[i]==0 and arr[i+1]==0:
                temp+=1
            elif arr[i]==0:
                temp+=1
                
                if temp>l_zero:
                    l_zero=temp
                temp=0
            else:
                pass
    except Exception:
        if arr[i]==0:
            temp+=1
            if temp>l_zero:
                    l_zero=temp
    finally:
        print(l_zero)



