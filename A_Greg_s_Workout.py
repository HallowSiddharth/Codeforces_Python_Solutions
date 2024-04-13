n=int(input())
chest=0

biceps=0

back=0

lst=list(map(int,input().rstrip().split()))
for i in range(n):
    if i%3==0:
        chest+=lst[i]
    elif i%3==1:
        biceps+=lst[i]
    else:
        back+=lst[i]
if biceps > max(chest,back):
    print("biceps")
elif chest > max(biceps,back):
    print("chest")
else:
    print("back")