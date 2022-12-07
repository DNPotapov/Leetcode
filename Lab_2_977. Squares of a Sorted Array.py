'''
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/description/
'''

class Solution(object):
    def merge(self, l_, r_):
        mass = []
        i = 0
        j = 0
        while i < len(l_) and j < len(r_):
            if l_[i] <= r_[j]:
                mass.append(l_[i])
                i += 1
            else:
                mass.append(r_[j])
                j += 1

        mass += l_[i:] + r_[j:]
        return mass


    def sort_merge(self, nums):
        left = nums[:len(nums) // 2]
        right = nums[len(nums) // 2:]

        if len(left) > 1:
            left = Solution.sort_merge(self, left)
        if len(right) > 1:
            right = Solution.sort_merge(self, right)

        return Solution.merge(self, left, right)


    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i]**2

        return Solution.sort_merge(self, nums)