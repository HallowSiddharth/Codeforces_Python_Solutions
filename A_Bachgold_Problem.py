n=int(input())
if n%2==0:
    c=n//2
    print(c)
    lst=['2' for i in range(c)]
else:
    c=n//2
    print(c)
    lst=['2' for i in range(c-1)]
    lst.append('3')
print(' '.join(lst))