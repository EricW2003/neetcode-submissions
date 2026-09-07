"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dic = {}
        copy = Node(head.val)
        
        dic = {head : copy}

        hd = head.next 
        tail = copy
        while hd:
            tail.next = Node(hd.val)
            tail = tail.next
            dic[hd] = tail
            hd = hd.next
        
        tail = copy
        hd = head
        while hd:
            if hd.random:
                tail.random = dic[hd.random]
            tail =tail.next
            hd = hd.next
        return copy
        