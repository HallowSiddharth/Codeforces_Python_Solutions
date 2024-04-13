class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        copy = list(nums1[:m])
        tally = 0
        while i < m and j < n:
            
            if copy[i] > nums2[j]:
                nums1[tally] = nums2[j]
                j += 1
            else:
                nums1[tally] = copy[i]
                i += 1
            tally += 1
        if i < m:
            while i < m:
                nums1[tally] = copy[i]
                tally += 1
                i += 1
        if j < n:
            while j < n:
                nums1[tally] = nums2[j]
                j += 1
                tally += 1


s = Solution()
s.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
