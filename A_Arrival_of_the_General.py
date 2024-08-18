# create a swap operation
def swap(i, j, lst):
    lst[i], lst[j] = lst[j], lst[i]


n = int(input())
lst = list(map(int, input().rstrip().split()))

# maximum index
max_ind = 0
# minimum index
min_ind = 0
# total number of swaps
swaps = 0

max_el = lst[0]
min_el = lst[0]

for i in range(n):
    if lst[i] > max_el:
        max_el = lst[i]
        max_ind = i

    if lst[i] <= min_el:
        min_el = lst[i]
        min_ind = i

spare = 0
# check if there is a collion
if min_ind < max_ind:
    spare = -1

# calculating the number of swaps
max_swaps = max_ind - 0
min_swaps = n - 1 - min_ind
swaps = max_swaps + min_swaps + spare
# now we can go ahead and print our answer
print(swaps)
