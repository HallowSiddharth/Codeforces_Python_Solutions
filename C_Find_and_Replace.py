t=int(input())
for i in range(t):
    n=int(input())
    st=input()
    result="YES"
    d={}
    for i in range(n):
        if st[i] not in d:
            d[st[i]]=i
        else:
            if d[st[i]]%2 != i%2:
                result="NO"
    print(result)