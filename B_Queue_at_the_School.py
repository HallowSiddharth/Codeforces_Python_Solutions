n,t = list(map(int,input().rstrip().split()))
st = input()
lst = [i for i in st]

for _ in range(t):
    i = 1
    while i<n:
        if lst[i-1] == 'B' and lst[i] == "G":
            lst[i-1],lst[i] = lst[i],lst[i-1]
            i += 1 
        i += 1

print(''.join(lst))

