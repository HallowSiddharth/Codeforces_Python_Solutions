n, m = list(map(int, input().rstrip().split()))
# task list
a = list(map(int, input().rstrip().split()))

time_taken = 0

# initially Xenia is at position 1
time_taken += a[0] - 1

for i in range(m - 1):
    # if next element is greater than current element
    if a[i + 1] >= a[i]:
        time_taken += a[i + 1] - a[i]
    # reset to start then from there (clockwise)
    else:
        time_taken += n - a[i] + a[i + 1]

print(time_taken)
