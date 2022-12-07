'''
237. Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/
'''

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        cur.val = cur.next.val
        cur.next = cur.next.next