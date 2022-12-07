'''
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
'''

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lst = set()
        cur = headA
        while cur:
            lst.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in lst:
                return cur
            cur = cur.next
        return None