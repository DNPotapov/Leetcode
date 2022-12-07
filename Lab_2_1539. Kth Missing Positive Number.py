'''
1539. Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number/
'''

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        res = []

        for i in range(1, max(arr)):
            if i not in arr and len(res) != k:
                res.append(i)
        if not res:
            return max(arr) + k
        if len(res) == k:
            return max(res)
        else:
            return (max(arr) + (k - len(res)))