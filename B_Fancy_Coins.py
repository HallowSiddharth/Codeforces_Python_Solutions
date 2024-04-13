t = int(input())
for i in range(t):
    m, k, a1, ak = list(map(int, input().rstrip().split()))
    ans = 0
    if a1 >= k:
        if ak * k > m:
            if a1 < m % ak:
                print((m % ak) - a1)
            else:
                print(0)

        else:
            rem = m - ak * k
            if a1 >= rem:
                print(0)
            else:
                rem -= a1
                if rem <= k:
                    print(1)
                else:
                    ans = 0
                    quo = rem // k
                    ans += quo
                    rem2 = rem % k
                    ans += rem2
                    print(ans)

    else:
        quo = m // k
        if quo > ak:
            ans += quo - ak
        rem = m % k
        if rem > a1:
            ans += rem - a1
        print(ans)
