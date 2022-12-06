'''
268. Missing Number
https://leetcode.com/problems/missing-number/
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) != len(nums):
            return len(nums)
        res = (1 + len(nums)) * len(nums) / 2 - sum(nums)
        return res