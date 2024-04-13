t=int(input())
d={}
for i in range(t):
    st=input()
    if st not in d:
        d[st]=1
        print("OK")
    else:
        print(f"{st}{d[st]}")
        d[st]+=1