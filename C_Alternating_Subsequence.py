t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    sequence = []
    for i in range(n):
        if sequence == []:
            sequence.append(lst[i])
        elif (
            (lst[i] > 0 and sequence[-1] < 0)
            or lst[i] < 0
            and (lst[i] < 0 and sequence[-1] > 0)
        ):
            sequence.append(lst[i])
        else:
            if lst[i] > sequence[-1]:
                sequence.pop(-1)
                sequence.append(lst[i])
    print(sum(sequence))
