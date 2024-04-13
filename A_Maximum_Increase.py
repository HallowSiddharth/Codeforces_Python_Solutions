n = int(input())
lst = list(map(int, input().rstrip().split()))
ml = 0
temp = 1
#fa = []
#ta = [lst[0]]
for i in range(1, n):
    #print("CHeckin:", lst[i])
    if lst[i] > lst[i - 1]:
        #print(lst[i], ">", lst[i - 1])
        #ta.append(lst[i])
        temp += 1
        #print("Temp val:", temp)
    else:
        if temp > ml:
            ml = temp
            temp = 1
            # if len(ta) > len(fa):
            #     fa = list(ta)
            # ta = [lst[i]]
        else:
            temp = 1

if temp >= ml:
    ml = temp
    temp = 0
#print(fa)
print(ml)
