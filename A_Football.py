n = int(input())
goals = {}
for _ in range(n):
    team = input()
    if team in goals:
        goals[team] += 1
    else:
        goals[team] = 1

max_goals = 0
winner = ""
for team in goals:
    if goals[team] > max_goals:
        max_goals = goals[team]
        winner = team

print(winner)
