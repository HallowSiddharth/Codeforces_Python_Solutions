n = int(input())
x = 0
for _ in range(n):
    st = input()
    if st == "X--" or st == "--X":
        x -= 1
    elif st == "X++" or st == "++X":
        x += 1

print(x)
