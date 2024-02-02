# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        count=0
        while current:
            count+=1
            current=current.next
        current=None
        new=head
        for i in range(count//2):
            new=new.next
        return new