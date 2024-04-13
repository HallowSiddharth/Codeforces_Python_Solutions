a, b, n = list(map(int, input().rstrip().split()))

a = str(a)
flag = True
# for _ in range(n):
#     ans = False
#     for i in "0123456789":
#         tem = a + i
#         if int(tem) % b == 0:
#             a = tem
#             ans = True
#             break
#     if not ans:
#         flag = False
#         break

# if not flag:
#     print(-1)
# else:
#     print(a)
ans = False
for i in "0123456789":
    tem = a + i
    if int(tem) % b == 0:
        a = tem
        ans = True
        break
if not ans:
    print(-1)
else:
    print(a + ("0" * (n - 1)))
