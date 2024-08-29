n = int(input())
dx = {}
dy = {}
points = []
for _ in range(n):
    x, y = list(map(int, input().rstrip().split()))
    points.append((x, y))
    if x not in dx:
        # [min, max]
        dx[x] = [y, y]
    else:
        # if x is in dx
        # check is x is the minim or max
        if y < dx[x][0]:
            dx[x][0] = y
        if y > dx[x][1]:
            dx[x][1] = y

    if y not in dy:
        dy[y] = [x, x]
    else:
        if x < dy[y][0]:
            dy[y][0] = x
        if x > dy[y][1]:
            dy[y][1] = x
sper_points = 0

for x, y in points:
    # check if x value is the max or the min
    # let's check for the x point
    # min is 0th index, max is 1st index
    if y > dx[x][0] and y < dx[x][1]:
        # now check for the y point
        if x > dy[y][0] and x < dy[y][1]:
            sper_points += 1
print(sper_points)
