'''
560. Subarray Sum Equals K (+)
https://leetcode.com/problems/subarray-sum-equals-k/
'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        summa = 0
        res = 0
        dict_ = {0: 1}
        for item in nums:
            summa += item
            res += dict_.get(summa - k, 0)
            dict_[summa] = dict_.get(summa, 0) + 1
        return res