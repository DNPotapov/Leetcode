'''
1290. Convert Binary Number in a Linked List to Integer
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
'''

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        res = ""
        while (cur.next):
            res += str(cur.val)
            cur = cur.next
        res += str(cur.val)
        return int(res,2)