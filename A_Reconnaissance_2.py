n = int(input())
lst = list(map(int, input().rstrip().split()))

"""
Logic:
1. Set minimum as difference between last and first element
2. then iterate over the list, comparing each two elements
3. Incase it is lower, update the minimum distance and the answer and repeat
"""

min_difference = abs(lst[0] - lst[-1])
ans = [1,n]
for i in range(1,n):
    if abs(lst[i] - lst[i-1]) < min_difference:
        ans = [i+1 , i]
        min_difference = abs(lst[i] - lst[i-1])
print(ans[0] , ans[1])