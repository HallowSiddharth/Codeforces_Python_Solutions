"""
Logic:
1. we take string input
2. We check if string starts with 1 and 444 is not there, as
    14 144 1414 1144 are all possible combinations. 4444 is not (minimum 3 4s together not allowed)
3. we check if 1 or 4 is not in the string, if yes we break and declare failure
4. else, success
"""

st = input()
ans = "YES"
if not st.startswith('1') or '444' in st:
    ans = "NO"
else:
    for i in st:
        if i not in ["1", "4"]:
            ans = "NO"
            break
print(ans)
