class Solution:
    def myAtoi(self, s: str) -> int:
        upper_l = 2**31 - 1
        lower_l = -1 * 2**31
        st = ""
        res = True
        start = 0
        # if s[0] == "-":
        #     st += "-"
        #     start = 1
        # elif s[0] == "+":
        #     start = 1
        # else:
        #     start = 0
        for i in s[start:]:
            if (i == "-" or i == "+") and st == "":
                st += i
            elif i.isdigit():
                st += i
            elif i.isdigit() == False and i != " ":
                break
                flag = False
        if st == "":
            return 0

        else:
            # if int(st) > upper_l:
            #     return upper_l
            # elif int(st) < lower_l:
            #     return lower_l
            return st


s = Solution()
print(s.myAtoi("-+12"))
