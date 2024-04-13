t=int(input())
for i in range(t):
    st=input()
    s=0
    ref="codeforces"
    for i in range(len(st)):
        if st[i]!=ref[i]:
            s+=1

    print(s)
