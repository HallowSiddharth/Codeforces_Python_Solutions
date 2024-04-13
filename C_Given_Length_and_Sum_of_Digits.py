m,s=list(map(int,input().rstrip().split()))


if m==1 and s==0:
    print(0,0)

elif s/m>9 or s==0 :
    print(-1,-1)

elif m>s:
    s1='1'+'1'*(s-1)+('0'*(m-s))
    s2='1'+('0'*(m-s))+'1'*(s-1)
    print(s2,s1)

elif m==1:
    print(s,s)

else:
    p9=s%9
    q1=s//9
    s1='1'
    snew=s-1
    s2=(str(9)*(q1))+str(p9)+'0'*(m-1-q1)
    print(s1,s2)
