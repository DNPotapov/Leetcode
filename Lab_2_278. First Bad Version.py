'''
278. First Bad Version
https://leetcode.com/problems/first-bad-version/
'''

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        start = 1
        end = n
        middle = int((start + end) / 2)
        while start <= end:
            if isBadVersion(middle):
                end = middle - 1
            else:
                start = middle + 1
            middle = int((start + end) / 2)
        return start