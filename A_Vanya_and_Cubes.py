n = int(input())
levels = 0
i = 1
level_cubes = 0
while n > 0:
    level_cubes += i
    i += 1
    n -= level_cubes
    if n >= 0:
        levels += 1
    else:
        break
print(levels)
