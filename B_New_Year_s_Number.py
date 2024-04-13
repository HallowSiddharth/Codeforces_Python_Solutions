t=int(input())
for i in range(t):
    n=int(input())
    ans="YES"
    while n>=2020:
        if n%2021 != 0:
            n-=2020
        else:
            break
    if n!=0 and n<2020:
        ans="NO"
    print(ans)

