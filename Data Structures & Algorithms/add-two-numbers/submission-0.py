# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        hd1 = l1
        hd2 = l2
        
        while hd1.next and hd2.next:
            val1 = hd1.val
            val2 = hd2.val
            hd1.val = (val1+val2+carry)%10
            hd2.val = (val1+val2+carry)%10
            carry = (val1+val2+carry)//10
            hd1 = hd1.next
            hd2 = hd2.next

        val1 = hd1.val
        val2 = hd2.val
        hd1.val = (val1+val2+carry)%10
        hd2.val = (val1+val2+carry)%10
        carry = (val1+val2+carry)//10

        if not hd1.next and not hd2.next and carry!=0:
            hd1.next = ListNode(carry)
            return l1
        print("hey2")
        if hd1.next:
            while hd1.next:
                hd1 = hd1.next
                val1 = hd1.val
                hd1.val = (val1 +carry)%10
                carry = (val1 +carry)//10
            if carry:
                hd1.next = ListNode(carry)
            return l1
        else:
            while hd2.next:
                hd2 = hd2.next
                val2 = hd2.val
                hd2.val = (val2 +carry)%10
                carry = (val2 +carry)//10
            if carry:
                hd2.next = ListNode(carry)
            return l2

        
