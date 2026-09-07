# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def inverseList(head):
    tail = None
    while head:
        v = head.next
        head.next = tail
        tail = head
        head = v
    return tail
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        inverted = inverseList(slow)
        head1, tail1 = head, head.next
        head2, tail2 = inverted, inverted.next

        while tail2:

            head1.next = head2
            head1 = tail1
            tail1 = tail1.next

            head2.next = head1
            head2 = tail2
            tail2 = tail2.next

        head1.next = head2
        head2.next = None




