'''
2181. Merge Nodes in Between Zeros
https://leetcode.com/problems/merge-nodes-in-between-zeros/
'''

class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        res = ListNode(None)
        lst = res
        count = 0
        while cur:
            if cur.val != 0:
                count += cur.val
            else:
                lst.next = ListNode(count)
                lst = lst.next
                count = 0
            cur = cur.next
        return res.next.next