# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_head=None
        hd=head
        while hd is not None:
            tl=hd.next
            hd.next=reverse_head
            reverse_head=hd
            hd=tl
        return reverse_head