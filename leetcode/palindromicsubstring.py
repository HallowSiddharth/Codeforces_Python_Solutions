def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s
    max_str = ""
    for i in range(len(s)):
        for j in range(len(s), -1, -1):
            # print(s[i:j])
            print(s[j - 1 : i - 1 : -1])
            if i == 0:
                if s[i:j] == s[j - 1 :: -1]:
                    # print(s[i:j])
                    if len(s[i:j]) > len(max_str):
                        max_str = s[i:j]
            else:
                if s[i:j] == s[j - 1 : i - 1 : -1]:
                    print(s[i:j])
                    if len(s[i:j]) > len(max_str):
                        max_str = s[i:j]

    return max_str


print(longestPalindrome("bb"))
