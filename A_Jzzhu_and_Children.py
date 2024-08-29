import math

n, m = list(map(int, input().rstrip().split()))
# number of candies each child wants
lst = list(map(int, input().rstrip().split()))
# find the number of servings required for each child
servings = []
for i in lst:
    serve = math.ceil(i / m)
    servings.append(serve)

# we need to find the maximum value from the right most part
# we need it's position (n-i)
ma = max(servings)
# reversing the list
servings.reverse()
# find out the index i
i = servings.index(ma)
# finding out the position
ans = n - i
print(ans)
