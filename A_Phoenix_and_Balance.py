t=int(input())
for i in range(t):
    n=int(input())
    arr=[]
    for i in range(1,n+1):
        arr.append(2**i)
    arr1=[]
    arr2=[]
    for i in range(n//2):
        if i%2==0:
            arr1.extend([arr[i],arr[-1-i]])
        else:
            arr2.extend([arr[i],arr[-1-i]])
    print(abs(sum(arr1)-sum(arr2)))