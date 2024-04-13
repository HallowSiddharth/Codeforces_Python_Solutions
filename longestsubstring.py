# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         #code for length of longest repeating substring
#         start = 0
#         end = 1
#         ct = 0
#         temp = 0
#         while start < len(s) - 1:
#             print(s[start:end], start)
#             if s.count(s[start:end]) > 1:
#                 end += 1
#                 temp += 1
#             else:
#                 ct = max(temp,ct)
#                 temp = 0
#                 start += 1
#                 end = start + 1
#         return ct
                

# s = Solution()
# print(s.lengthOfLongestSubstring("pwwkew"))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = [_ for _ in s]
        i = 0
        end = 0
        st = ""
        temp = ""
        while end < len(s) - 1 :
            if lst[i] not in st:
                temp += lst[i]
                end += 1 
            else:
                if len(temp)> len(st):
                    st = temp
                ind = lst.index()





s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))