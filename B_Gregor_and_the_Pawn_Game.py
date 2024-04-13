t = int(input())
for i in range(t):
    n = int(input())
    enemies_st = input()
    enemies = [int(pos) for pos in enemies_st]
    answer = 0
    gregor = input()
    for pawn in range(n):

        if gregor[pawn] == "1":
            if enemies[pawn] == 0:
                answer += 1
            elif pawn > 0 and enemies[pawn - 1] == 1:
                answer += 1
                enemies[pawn - 1] = 2
            elif pawn < n - 1 and enemies[pawn + 1] == 1:
                answer += 1
                enemies[pawn + 1] = 2
    print(answer)
