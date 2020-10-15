# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """Brute force with O(2N) approach
        
        temp = head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        mid = (cnt // 2) + 1
        iteration = 1
        while(head and iteration != mid):
            head = head.next
            iteration += 1
        return head
        
        """
        """Optimed approach with 2Ptrs and O(N/2)"""
        temp = head
        ptr1 = head
        ptr2 = head
        while(ptr2 and ptr2.next != None):
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next      
        return ptr1
    
        