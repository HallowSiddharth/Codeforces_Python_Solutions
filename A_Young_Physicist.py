n = int(input())
x = 0
y = 0
z = 0
for _ in range(n):
    vec = list(map(int, input().rstrip().split()))
    x += vec[0]
    y += vec[1]
    z += vec[2]

if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")
