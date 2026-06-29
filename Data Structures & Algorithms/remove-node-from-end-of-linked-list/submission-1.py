# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        arr = []
        ptr = dummy
        while(ptr):
            arr.append(ptr)
            ptr = ptr.next
        node = len(arr) - n
        arr[node-1].next = arr[node].next
        return dummy.next
        
            

        