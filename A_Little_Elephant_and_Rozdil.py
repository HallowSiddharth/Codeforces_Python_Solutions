"""
Logic
1. Since we just need to find if there is a duplication of minimum element, no need for sorting.
2. No need of frequency histogram, since even 1 duplication would mean failure
3. Since we need just the index, we keep track of minimum index, not minimum element.
"""

n = int(input())
lst = list(map(int, input().rstrip().split()))
minimum = 0
ans = None
for i in range(1, n):
    if lst[i] < lst[minimum]:
        minimum = i
    # elif lst[i] == lst[minimum]:
    #     print(lst[minimum])
    #     print(lst[i])
    #     print(i)
    #     ans = "Still Rozdil"
if lst.count(lst[minimum]) == 1:
    print(minimum + 1)
else:
    print("Still Rozdil")
