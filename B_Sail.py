t, sx, sy, ex, ey = list(map(int, input().rstrip().split()))
tlst = list(input())
dx = ex - sx
dy = ey - sy
if dx < 0:
    xdirection = "W"
elif dx > 0:
    xdirection = "E"
else:
    xdirection = None

if dy < 0:
    ydirection = "S"
elif dy > 0:
    ydirection = "N"
else:
    ydirection = None

dx = abs(dx)
dy = abs(dy)
ans = -1

for i in range(t):
    if tlst[i] == xdirection:
        dx -= 1
    if tlst[i] == ydirection:
        dy -= 1

    if dx <= 0 and dy <= 0:
        ans = i + 1
        break

print(ans)

# ans = -1
# for i in range(t):
#     if tlst[i] == "N":
#         if sy < ey:
#             sy += 1
#     if tlst[i] == "S":
#         if sy > ey:
#             sy += 1
#     if tlst[i] == "E":
#         if sx < ex:
#             sx += 1
#     if tlst[i] == "W":
#         if sx > ex:
#             sx -= 1

#     if ex == sx and ey == sy:
#         ans = i + 1
#         break
# print(ans)
