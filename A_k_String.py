"""
Already submitted, providing documentation
Logic:
1. take frequency histogram
2. check if all elements' count in the histogram is divisible by k
3. If no , -1 else proceed
4. take st, add frequency/k for each element to the string to find basic string
5. multiply that by k to get final answer
"""


k = int(input())
string = input()
d = {}
for i in string:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
case = True
for i in d:
    if d[i] / k != d[i] // k:
        case = False

if case:
    st = ""
    for i in d:
        st += i * (d[i] // k)
    print(st * k)
else:
    print(-1)
