k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
total = 0
for i in range(1, d + 1):
    if i % l == 0 or i % k == 0 or i % m == 0 or i % n == 0:
        total += 1

print(total)
