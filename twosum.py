import random


class Solution:
    def quicksort(self, lst):
        if len(lst) <= 1:
            return lst
        else:
            pivot = random.choice(lst)
            lst.remove(pivot)
            right = []
            left = []
            for i in lst:
                if i > pivot:
                    right.append(i)
                else:
                    left.append(i)
            return self.quicksort(left) + [pivot] + self.quicksort(right)

    def binary_search(self, low, high, arr, key):
        if low > high:
            return False
        else:
            mid = (low + high) // 2
            el = arr[mid]

            if key == el:
                return True
            elif key > el:
                return self.binary_search(mid + 1, high, arr, key)
            else:
                return self.binary_search(low, mid - 1, arr, key)

    def twoSum(self, nums, target: int):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        answer = []
        ognums = list(nums)
        temp_nums = self.quicksort(nums)
        for i in range(len(nums)):
            element = temp_nums[i]
            remaining = target - temp_nums[i]
            if remaining != element or (remaining == element and d[remaining] == 2):
                if self.binary_search(0, len(nums), temp_nums, remaining) == True:
                    answer = [element, remaining]
                    break
        x = answer[0]
        y = answer[1]
        if x == y:
            indx = ognums.index(x)
            rev = list(ognums[::-1])
            indy = len(ognums) - rev.index(y) - 1

        return [indx, indy]


a = Solution()
print(a.twoSum(nums=[3, 3], target=6))
