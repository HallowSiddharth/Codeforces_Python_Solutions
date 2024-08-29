"""
Logic
1. Since we just need to find if there is a duplication of minimum element, no need for sorting.
2. No need of frequency histogram, since even 1 duplication would mean failure
3. Since we need just the index, we keep track of minimum index, not minimum element.
"""

n = int(input())
lst = list(map(int, input().rstrip().split()))

min_el = lst[0]
# position value : output
ans = 1

for i in range(1, n):
    if lst[i] < min_el:
        min_el = lst[i]
        ans = i + 1
    elif lst[i] == min_el:
        # repition of minimum elements
        ans = "Still Rozdil"
    else:
        continue

print(ans)
