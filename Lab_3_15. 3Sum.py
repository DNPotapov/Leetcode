'''
15. 3Sum (+)
https://leetcode.com/problems/3sum/
'''

class Solution:
    def threeSum(self, nums):
        nums.sort()
        set_nums = set()
        res = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                summa = - nums[i] - nums[j]
                if summa in set_nums:
                    res.add((summa, nums[i], nums[j]))
            set_nums.add(nums[i])
        return res