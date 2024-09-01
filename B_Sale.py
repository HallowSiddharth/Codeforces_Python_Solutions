n, m = list(map(int, input().rstrip().split()))
prices = list(map(int, input().rstrip().split()))

earnings = 0
prices.sort()

for i in range(m):
    # check if it is a negative value
    if prices[i] < 0:
        earnings += prices[i]
    else:
        break

print(earnings * -1)
