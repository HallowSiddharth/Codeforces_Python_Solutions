class Solution:
    def longestCommonPrefix(self, strs) -> str:
        sample = strs[0]
        ans = ""
        finalStatus = True
        for letter_ind in range(len(sample)):
            if finalStatus:
                letter = sample[letter_ind]
                status = True
                for string in strs:
                    if len(string) <= letter_ind:
                        status = False
                        finalStatus = False
                        break
                    elif string[letter_ind] != letter:
                        status = False
                        finalStatus = False
                        break
                if status:
                    ans = ans + letter
                else:
                    break
            else:
                break
        return ans


s = Solution()
print(s.longestCommonPrefix(["ab", "a"]))
