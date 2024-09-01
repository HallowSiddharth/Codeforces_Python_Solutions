"""
Logic
1. Take inputs.
2. iterate 2 for loops and divide all b's by all a's to see the 
available gears.
3. add the gears to the list, find out the max element.
4. find the count of the max element and print to the user.
"""

n = int(input())
a = list(map(int, input().rstrip().split()))
m = int(input())
b = list(map(int, input().rstrip().split()))
max_gear = 0
gear_count = 0

for i in a:
    for j in b:
        # check if it is an integer gear
        if j / i == j // i:
            gear = j // i
            if gear > max_gear:
                max_gear = gear
                gear_count = 1
            elif gear == max_gear:
                gear_count += 1
            else:
                continue

print(gear_count)
