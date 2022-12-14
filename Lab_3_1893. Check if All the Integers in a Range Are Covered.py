'''
1893. Check if All the Integers in a Range Are Covered (+)
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
'''

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ranges.sort(key = lambda x: x[0])
        for start, end in ranges:
            if left < start:
                return False
            if left <= end:
                left = end + 1
        return right < left