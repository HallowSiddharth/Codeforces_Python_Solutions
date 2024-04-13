t = int(input())
for _ in range(t):
    seq = input()
    stack = []
    ans = True
    # rbs check
    ans2 = True
    stack = []
    for i in seq:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack == []:
                stack.append(i)
                ans2 = False
                break
            elif stack[-1] == "?" or stack[-1] == "(":
                stack.pop(-1)
            else:
                stack.append(i)
                ans2 = False
                break
        else:
            if stack2 == []:
                    stack2.append(i)
            else:
                if stack2[-1] == "?":
                    stack2.pop(-1)
                else:
                    stack2.append(i)
    stack2 = []
    if stack != []:
        for i in stack:
            if i == "?":
                if stack2 == []:
                    stack2.append(i)
                else:
                    if stack2[-1] == "?":
                        stack2.pop(-1)
                    else:
                        stack2.append(i)
            else:
                stack2.append(i)

    # sq = list(set(stack))
    if stack2 == []:
        print("YES")
    else:
        print("NO")
