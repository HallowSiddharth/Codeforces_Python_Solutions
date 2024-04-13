t=int(input())
for i in range(t):
    n=int(input())
    rem=n%7
    if rem > 7-rem:
        n+=7-rem
    else:
        n-=rem
    print(n) 