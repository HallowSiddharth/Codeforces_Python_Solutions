n=int(input())
lst=list(map(int,input().rstrip().split()))
segct=0
seg=False
segst=1
segend=1
ans="yes"
if n==1:
    print("yes")
    print(segst,segend)
else:
    for i in range(n-1):
        if lst[i]>lst[i+1]:
            if seg==False:
                seg=True
                segst=i+1

        if seg and lst[i]<lst[i+1]:
            segend=i+1
            segct+=1
            seg=False
            if lst[i+1]<lst[segst-1]:
                ans="no"


    if lst[i+1]<lst[i] and seg:

        segct+=1
        segend=i+2
        if lst[i+1]<lst[segst-2]:
                ans="no"



    if ans=='no':
        print('no')

    elif segct<=1:
        print("yes")
        print(segst,segend)
    else:
        print("no")