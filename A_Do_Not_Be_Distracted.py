t=int(input())
for i in range(t):
    n=int(input())
    st=input()
    tasks=[]
    result="YES"
    for i in range(1,n):
        if st[i]!=st[i-1]:
            tasks.append(st[i-1])
        if st[i] in tasks:
            result="NO"
    print(result)
        