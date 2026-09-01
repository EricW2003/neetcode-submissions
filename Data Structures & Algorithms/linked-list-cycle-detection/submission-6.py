# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head ==None:
            return False
        visited = set()
        hd = head.val
        tail = head.next
        while tail:
            visited.add(head)
            if tail in visited:
                return True
            head, tail = tail, tail.next
        return False
