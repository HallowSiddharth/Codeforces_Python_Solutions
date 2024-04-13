st = input()
d = {}
for i in st:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
no = 0
for i in d:
    no += d[i] % 2

if (no - 1) % 2 == 0 or no == 0:
    print("First")
else:
    print("Second")
