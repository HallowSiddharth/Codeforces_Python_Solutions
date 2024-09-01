t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    # assume answer is yes
    ans = "Yes"
    length = len(s)
    # checking if perfect
    if length**0.5 != int(length**0.5):
        ans = "No"
    else:
        # perfect square
        # find out r, r = c
        r = int(length**0.5)
        for i in range(0, n, r):
            line = s[i : i + r]
            # print(line)
            if i == 0 or i == n - r:
                # top row and bottom row edge condition
                if line != "1" * r:
                    ans = "No"
                    break
            else:
                # condition to check if 0 is inside or not
                if line != "1" + "0" * (r - 2) + "1":

                    ans = "No"
                    break
    print(ans)
