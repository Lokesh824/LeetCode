# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Algo steps:
            * Save the node's next add 
            * Move the prev value to the current node next
            * make the current node as prev
            * move to the next node
        """
        curr = head
        prev = None
        nxt = None
        while(curr):
            "store the next part of current node is nxt "
            nxt = curr.next
            "Now making the current node next as prev "
            curr.next = prev
            "Make the current node as prev for next iteration"
            prev = curr
            "move to the next node"
            curr = nxt
            
        return prev
        