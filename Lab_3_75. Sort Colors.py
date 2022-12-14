'''
75. Sort Colors (+)
https://leetcode.com/problems/sort-colors/
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        dict_ = {}
        res = []
        for x in nums:
            dict_[x] = 1 + dict_.get(x, 0)
        for i in range(3):
            res += [i] * dict_.get(i, 0)
        for i in range(len(res)):
            nums[i] = res[i]
