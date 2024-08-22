lst = list(input())
# convert this list into a set
ans = set(lst)
if len(ans) % 2 == 0:
    # even case: female
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
