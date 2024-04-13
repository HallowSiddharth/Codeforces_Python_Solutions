t = int(input())
for case in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    lst.sort()
    mid = len(lst) // 2
    first_half = lst[:mid]
    second_half = lst[mid:]
    answer = []
    for i in range(len(first_half)):
        if i % 2 == 0:
            answer.append(second_half[0])
            second_half.pop(0)
        else:
            answer.append(first_half[0])
            first_half.pop(0)
    if second_half != []:
        answer.extend(second_half[:])
    if first_half != []:
        answer.extend(first_half[:])
    answer = [str(i) for i in answer]
    print(" ".join(answer))
