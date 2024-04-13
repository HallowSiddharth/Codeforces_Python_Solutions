def finddiv(n):
    div=0
    before=0
    while n>0:
        div+=1
        before=n
        n-= 2**(div-1)*5
    return [div,before]
import math
n=int(input())
div,before=finddiv(n)
lst=["Sheldon","Leonard","Penny","Rajesh","Howard"]
print(lst[math.ceil(before/(2**(div-1)))-1])
