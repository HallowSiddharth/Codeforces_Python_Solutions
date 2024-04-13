#hi2
t=int(input())
for i in range(t):
    n=int(input())
    result="YES"
    d={q:0 for q in "abcdefghijklmnopqrstuvwxyz"}
    for j in range(n):
        st=input()
        for j in st:
            d[j]+=1
    for k in d:
        if d[k]%n!=0:
            result="NO"
    print(result)