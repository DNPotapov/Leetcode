'''
852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/
'''

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 3:
            return -1
        start = 0
        end = len(arr) - 1
        middle = (start + end) // 2
        while start <= end:
            if arr[middle] > arr[middle + 1] and arr[middle] > arr [middle - 1]:
                return middle
            elif arr[middle] > arr[middle-1]:
                start = middle
            else:
                end = middle
            middle = (start + end) // 2