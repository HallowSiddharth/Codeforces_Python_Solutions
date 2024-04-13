#quick sort
def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        arr.pop(0)
        grt=[]
        ltl=[]
        for i in arr:
            if i>pivot:
                grt.append(i)
            else:
                ltl.append(i)
        return quicksort(ltl)+[pivot]+quicksort(grt)

print(quicksort([5,2,1,3,-1,2,-6]))