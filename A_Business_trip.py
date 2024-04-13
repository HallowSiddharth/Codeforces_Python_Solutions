def rev_quicksort(arr):
    if len(arr)<=1:
        return arr

    else:
        pivot=arr[len(arr)//2]
        arr.remove(pivot)
        grt=[]
        lsr=[]
        for i in arr:
            if i>pivot:
                grt.append(i)
            else:
                lsr.append(i)
        return rev_quicksort(grt)+[pivot]+rev_quicksort(lsr)


k=int(input())
lst=list(map(int,input().rstrip().split()))
a=rev_quicksort(lst)
s=0
ct=0
for i in a:
    if s>=k:
        break
    else:
        s+=i
        ct+=1
if s>=k:
    print(ct)
else:
    print(-1)