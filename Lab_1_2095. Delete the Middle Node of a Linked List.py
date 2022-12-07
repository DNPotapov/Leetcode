'''
2095. Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
'''

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        count = count // 2
        if count == 0:
            head = None
            return head
        cur = head
        while ((count - 1) > 0):
            cur = cur.next
            count = count - 1
        cur.next = cur.next.next
        return head