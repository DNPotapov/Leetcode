'''
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/
'''

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode(None)
        cur = head
        s = res
        while cur:
            if cur.val != val:
                s.next = cur
                s = s.next
            else:
                s.next = cur.next
            cur = cur.next
        return res.next