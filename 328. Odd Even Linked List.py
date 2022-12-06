'''
328. Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/
'''

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = ListNode(None)
        save = ListNode(None)
        cur = head
        s1 = res
        s2 = save
        count = 1
        while cur:
            if count%2 == 0:
                s2.next = ListNode(cur.val)
                s2 = s2.next
            else:
                s1.next = ListNode(cur.val)
                s1 = s1.next
            cur = cur.next
            count += 1
        s1.next = save.next
        return res.next