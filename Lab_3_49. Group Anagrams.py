'''
49. Group Anagrams (+)
https://leetcode.com/problems/group-anagrams/description/
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for word in strs:
            elem = "".join(sorted(word))
            if elem in res:
                res[elem].append(word)
            else:
                res[elem] = [word]
        return res.values()