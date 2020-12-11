# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse(head):
            prev_node = None
            
            while head:
                next_node = head.next
                head.next = prev_node
                prev_node = head
                head = next_node
            return prev_node
    
        fast = slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        fast = head
        slow = reverse(slow)
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True