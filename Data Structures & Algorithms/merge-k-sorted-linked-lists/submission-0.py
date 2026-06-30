# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        l1 = lists[0]
        for i in range(1, len(lists)):
            l2 = lists[i]
            dummy = ListNode()
            ptr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    ptr.next = l1
                    l1 = l1.next
                else:
                    ptr.next = l2
                    l2 = l2.next
                ptr = ptr.next
            if l1:
                ptr.next = l1
            else:
                ptr.next = l2
            l1 = dummy.next
        return l1

            

        