t=int(input())
for i in range(t):
    s=input()
    c=input()
    ind=-1
    for i in range(len(s)):
        if s[i]==c:

            if ind==-1:
                ind=i
            elif ind%2!=0:
                ind=i
    if ind%2==0 and ind!=-1:
        print("YES")
    else:
        print("NO")
