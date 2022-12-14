'''
1. Two Sum (+)
https://leetcode.com/problems/two-sum/
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for index, item in enumerate(nums):
            if item in res:
                return[res[item], index]
            res[target - item] = index
        return res