class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        output = True
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if stack == []:
                    output = False
                else:
                    if (char == ")" and stack[-1] == "(") or (char == "}" and stack[-1] == "{") or (char == "]" and stack[-1] == "["):
                        stack.pop(-1)
                    else:
                        output = False
        if stack != []:
            output = False
        print(stack)
        if output:
            return "true"
        else:
            return "false"


s = Solution()
print(s.isValid("]"))
