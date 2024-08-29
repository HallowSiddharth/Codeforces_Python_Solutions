n = int(input())
# total number of people
total = n + 1  # including Dima
lst = list(map(int, input().rstrip().split()))
# current finger out excluding Dima
curr = sum(lst)
# no of ways
ans = 0
# Dima has 1 to 5 fingers
# the total number of fingers will go from curr + 1 to curr + 5
for i in range(1, 6):
    # Case where Dima doesn't have to clean
    if (curr + i) % total != 1:
        ans += 1

print(ans)
