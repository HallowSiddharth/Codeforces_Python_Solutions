st = input()

ct = 0
for i in st:
    if i == "4" or i == "7":
        ct += 1

# checking where ct is lucky or not
ct = str(ct)
status = "YES"
for i in ct:
    if i not in "47":
        status = "NO"
        break

print(status)
