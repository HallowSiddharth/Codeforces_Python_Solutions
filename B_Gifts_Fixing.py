t = int(input())
for i in range(t):
    n = int(input())
    candies = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    min_c = min(candies)
    min_o = min(oranges)
    moves = 0
    for i in range(n):
        c = candies[i] - min_c
        o = oranges[i] - min_o
        moves += max(c, o)
    print(moves)
