'''
205. Isomorphic Strings (+)
https://leetcode.com/problems/isomorphic-strings/
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        dict_t = {}
        for item_s, item_t in zip(s, t):
            if item_s in dict_s and dict_s[item_s] != item_t or item_t in dict_t and dict_t[item_t] != item_s:
                return False
            dict_s[item_s] = item_t
            dict_t[item_t] = item_s
        return True

