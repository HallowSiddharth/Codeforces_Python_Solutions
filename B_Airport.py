"""
n - number of passengers
m - number of planes
"""
n, m = list(map(int, input().rstrip().split()))
planes = list(map(int, input().rstrip().split()))
planes_copy = list(planes)
min_cost = 0
max_cost = 0
for i in range(n):
    temp_max = planes.index(max(planes))
    max_cost += planes[temp_max]
    if planes[temp_max] > 1:
        planes[temp_max] -= 1
    else:
        planes.pop(temp_max)

for i in range(n):
    temp_min = planes_copy.index(min(planes_copy))
    min_cost += planes_copy[temp_min]
    if planes_copy[temp_min] > 1:
        planes_copy[temp_min] -= 1
    else:
        planes_copy.pop(temp_min)

print(max_cost, min_cost)
