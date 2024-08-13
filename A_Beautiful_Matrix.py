matrix = [[], [], [], [], []]

# initializing the matrix
for i in range(5):
    row = list(map(int, input().rstrip().split()))
    matrix[i] = row

# find the location of the 1
location_1 = []
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            location_1 = [i, j]

middle_x = 2
middle_y = 2

ans = abs(location_1[0] - middle_x) + abs(location_1[1] - middle_y)
print(ans)
