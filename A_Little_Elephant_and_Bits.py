number = input()
if number.startswith("0") or "0" not in number:
    print(number[1:])

else:
    ans = ""
    for i in range(len(number)):
        if number[i] == "1":
            ans += number[i]
        else:
            ans += number[i + 1 :]
            break

    print(ans)
