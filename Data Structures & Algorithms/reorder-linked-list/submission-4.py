# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        ptr = second
        while ptr:
            nxt = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = nxt
        ptr = head
        while prev:
            nxt = ptr.next
            rev_nxt = prev.next
            ptr.next = prev
            ptr = nxt
            prev.next = ptr
            prev = rev_nxt


