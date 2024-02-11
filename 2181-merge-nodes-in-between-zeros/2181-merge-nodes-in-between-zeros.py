# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        Dummy=ListNode(0)
        current = Dummy 
        res=0
        head=head.next
        while head:
            if head.val!=0:
                res+=head.val
            else:
                current.next=ListNode(res)
                res=0
                current=current.next
            head=head.next
        return Dummy.next
            