n=int(input())
for i in range(n):
    b=input()
    s=''
    s+=b[:2]
    if len(b)>2:
        for i in range(2,len(b),2):
            s+=b[i+1]
    print(s)

    