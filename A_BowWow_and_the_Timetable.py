def bin_conv(bnum):
    value = 0
    for i in range(len(bnum)):
        digit = bnum.pop()
        if digit == '1':
            value = value + pow(2, i)
    return value

lst=[]
a=list(input())
ba=bin_conv(a)
print(int((ba-1 )**0.25)+1)