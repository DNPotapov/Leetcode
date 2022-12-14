'''
128. Longest Consecutive Sequence.py
https://leetcode.com/problems/longest-consecutive-sequence/
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums_set = set(nums)
        for num in nums:
            count = 0
            if num - 1 in nums_set:
                continue
            while num in nums_set:
                num += 1
                count += 1
            res = max(res, count)
        return res