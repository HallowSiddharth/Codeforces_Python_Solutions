class Solution:
    def romanToInt(self, s: str) -> int:
        lst = [i for i in s]
        ans = 0
        while lst != []:
            if lst[0] == "M":
                lst.pop(0)
                ans += 1000
            elif lst[0] == "D":
                lst.pop(0)
                ans += 500
            elif lst[0] == "C":
                if len(lst) > 1 and lst[1] == "M":
                    lst.pop(0)
                    lst.pop(0)
                    ans += 900
                elif len(lst) > 1 and lst[1] == "D":
                    lst.pop(0)
                    lst.pop(0)
                    ans += 400
                else:
                    lst.pop(0)
                    ans += 100
            elif lst[0] == "L":
                lst.pop(0)
                ans += 50
            elif lst[0] == "X":
                if len(lst) > 1 and lst[1] == "L":
                    lst.pop(0)
                    lst.pop(0)
                    ans += 40
                elif len(lst) > 1 and lst[1] == "C":
                    lst.pop(0)
                    lst.pop(0)
                    ans += 90
                else:
                    lst.pop(0)
                    ans += 10
            elif lst[0] == "V":
                lst.pop(0)
                ans += 5
            elif lst[0] == "I":
                if len(lst) > 1 and len(lst) > 1 and lst[1] == "V":
                    lst.pop(0)
                    lst.pop(0)
                    ans += 4
                elif len(lst) > 1 and len(lst) > 1 and lst[1] == "X":
                    lst.pop(0)
                    lst.pop(0)
                    ans += 9
                else:
                    lst.pop(0)
                    ans += 1
        return ans


a = Solution()
print(a.romanToInt("MDLXX"))
