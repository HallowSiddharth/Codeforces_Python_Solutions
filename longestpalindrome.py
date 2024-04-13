class Solution:
    def isPalindrome(self, s: str):
        mid = len(s) // 2
        rev = s[mid + 1 :]
        if s[:mid] == rev[::-1]:
            return True
        else:
            return False

    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = len(s)
        st = ""
        temp = ""
        while start < len(s) - 1:
            print(start, end)
            print(st)
            print(s[start:end])
            if self.isPalindrome(s[start:end]):
                if len(st) < len(s[start:end]):
                    st = s[start:end]
                    start += 1
            elif start + 1 == end:
                end = len(s)
                start += 1
            else:
                end -= 1

        return st


s = Solution()
print(s.longestPalindrome("babad"))
