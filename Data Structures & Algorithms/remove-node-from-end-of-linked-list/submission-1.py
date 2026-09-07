# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def invert(head):
    if not head:
        return head
    tail = None
    while head:
        next = head.next
        head.next = tail
        tail = head
        head = next
    return tail
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = invert(head)
        tail = None
        nb = n-1
        while head:
            if nb==0:
                head = head.next
            else:
                next = head.next
                head.next = tail
                tail = head
                head = next
            nb-=1
        return tail


