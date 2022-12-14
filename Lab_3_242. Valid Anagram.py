'''
242. Valid Anagram (+)
https://leetcode.com/problems/valid-anagram/description/
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for item_s, item_t in zip(s, t):
            if item_s in dict_s:
                dict_s[item_s] += 1
            else:
                dict_s[item_s] = 1
            if item_t in dict_t:
                dict_t[item_t] += 1
            else:
                dict_t[item_t] = 1

        return dict_s == dict_t