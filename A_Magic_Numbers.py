"""
Logic:
1. we take string input
2. We check if string starts with 1 and 444 is not there, as
    14 144 1414 1144 are all possible combinations. 
    4444 is not (minimum 3 4s together not allowed)
3. we check if 1 or 4 is not in the string, if yes we break 
and declare failure
4. else, success
"""

st = input()
ans = "YES"

if st[0] != "1" or "444" in st:
    ans = "NO"
else:
    # it starts with 1, 444 not there
    # simply check if something other than 1 or 4 is there
    for i in st:
        if i not in ["1", "4"]:
            ans = "NO"
            break

print(ans)
