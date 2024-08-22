n = int(input())
# initial counts
left = {0: 0, 1: 0}
right = {0: 0, 1: 0}

for i in range(n):
    # state of the cupboard
    lft, rght = list(map(int, input().rstrip().split()))
    left[lft] += 1
    right[rght] += 1

# which is lesser in each case
total = 0
if left[0] > left[1]:
    total += left[1]
else:
    total += left[0]

if right[0] > right[1]:
    total += right[1]
else:
    total += right[0]

print(total)
