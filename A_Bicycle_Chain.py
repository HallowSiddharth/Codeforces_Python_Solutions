"""
Logic
1. Take inputs.
2. iterate 2 for loops and divide all b's by all a's to see the available gears.
3. add the gears to the list, find out the max element.
4. find the count of the max element and print to the user.
"""

a_n = int(input())
a_lst = list(map(int, input().rstrip().split()))
b_n = int(input())
b_lst = list(map(int, input().rstrip().split()))
gear_lst = []

for i in a_lst:
    for j in b_lst:
        if j / i == j // i:
            gear_lst.append(j // i)

max_gear_lst = max(gear_lst)
print(gear_lst.count(max_gear_lst))
