'''
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/submissions/
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        middle = start + (end - start) / 2
        while start < end:
            if nums[middle] > target:
                end = middle
            elif nums[middle] < target:
                start = middle + 1
            else:
                return middle
            middle = start + (end - start) / 2
        return start