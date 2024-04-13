t = int(input())
for _ in range(t):
    st = input()
    ans = []
    total = []
    status = {"1": False, "2": False, "3": False}
    # if (
    #     "123" in st
    #     or "231" in st
    #     or "312" in st
    #     or "132" in st
    #     or "213" in st
    #     or "321" in st
    # ):
    #     print(3)
    # else:
    for i in st:
        if i in ans:
            if i != ans[-1]:
                ans = ans[-1:]
                ans.append(i)
            else:
                temp2 = list(status.values())
                if temp2.count(True) != 1:
                    ans.append(i)
        else:
            status[i] = True
            ans.append(i)

        if status["1"] and status["2"] and status["3"]:
            total.append(ans)
            ans = ans[-2:]
            status["1"] = False
            status["2"] = False
            status["3"] = False
            status[ans[-1]] = True
            status[ans[-2]] = True

    # print(total)
    ml = float("inf")
    if total != []:
        for i in total:
            temp = len(i)
            if temp < ml:
                ml = temp
    else:
        ml = 0
    print(ml)
