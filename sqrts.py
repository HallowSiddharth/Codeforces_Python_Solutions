class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        for i in range(1, ((x + 1) // 2) + 2):
            if i**2 > x:
                return i - 1
            elif i**2 == x:
                return i


s = Solution()
print(s.mySqrt(4))
