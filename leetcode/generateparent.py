import itertools


class Solution:
    def generateParenthesis(self, n: int):
        lt = ["(" for _ in range(n)]
        rt = [")" for _ in range(n)]
        lst = lt + rt
        perm = itertools.permutations(lst[1:], 2 * n - 1)
        ans = []
        for i in perm:
            l = ["("] + list(i)
            print(l)
            stack = []
            # print(l)
            for j in l:
                if j == "(":
                    stack.append(j)
                else:
                    if stack == []:
                        stack.append(j)
                        break
                    elif stack[-1] == "(":
                        stack.pop(-1)
            if stack == []:
                ans.append("".join(l))
        return list(set(ans))


s = Solution()
s.generateParenthesis(3)
itertools.combinations()