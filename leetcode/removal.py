class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        try:
            ct = 0
            temp = nums[0]
            i += 1
            flag = False
            while True:
                print(nums)
                if nums[i] == temp and ct == 0:
                    ct += 1
                    i += 1
                    print(1)
                elif ct == 1 and nums[i] == temp:
                    # ct = 0
                    nums.pop(i)
                    print(2)
                else:

                    temp = nums[i]
                    ct = 0
                    i += 1
                    print(3)
        except Exception:
            print(nums)
            return len(nums)


s1 = Solution()
print(s1.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
