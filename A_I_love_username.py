n = int(input())
lst = list(map(int, input().rstrip().split()))
# max value
max_value = lst[0]
# min_value
min_value = lst[0]
total = 0
for i in lst[1:]:
    # amazing performances
    if i > max_value:
        max_value = i
        total += 1
    if i < min_value:
        min_value = i
        total += 1
print(total)
