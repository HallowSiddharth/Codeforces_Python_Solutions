n = int(input())
days = list(map(int, input().rstrip().split()))
# set a variable to point the current day
i = 1
while True:
    # calculate remaining  pages
    n -= days[i - 1]
    if n <= 0:
        break
    else:
        if i == 7:
            # reset i
            i = 1
        else:
            i += 1
print(i)
