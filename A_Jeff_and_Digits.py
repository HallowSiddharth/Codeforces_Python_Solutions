"""Already submitted but adding documentation
Logic
1. inorder for a number to be divisible by 9, it's sum must be divisible by 9
2. since all inputs are either 0 or 5, 9 5s makes 45.
3. so multiple of 9 5s, will give number divisible by 9.
4. for 90, we need multiple of 9 5s, and atleast 1 0.
5. since we can use less than the given numbers, we find out what is the closest multiple of 9 5s and then 
add number of zeros to it.
6. We must also lookout for edge cases 
    -> all 5s will mean no possible (-1)
    -> atleast 1 zero means 0
"""


n = int(input())
lst = list(map(int, input().rstrip().split()))
d = {}

for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

if 5 not in d:
    print(0)

elif 0 not in d:
    print(-1)

else:
    if d[5] >= 9 and d[0] > 0:
        print("5" * 9 * (d[5] // 9) + "0" * d[0])
    else:
        print(0)
