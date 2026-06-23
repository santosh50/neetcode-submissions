# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast != slow:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
        
        if fast:
            return True
        else:
            return False
        