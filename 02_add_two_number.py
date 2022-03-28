# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution2:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        first = ListNode(0, None)  # First Element is dummy node.
        now = first

        carry = 0
        v1 = 0
        v2 = 0

        while not (l1 is None and l2 is None):
            if l1 is None:
                v1 = 0
            else:
                v1 = l1.val
                l1 = l1.next

            if l2 is None:
                v2 = 0
            else:
                v2 = l2.val
                l2 = l2.next

            val = v1 + v2 + carry
            if val >= 10:
                now.next = ListNode(val - 10)
                carry = 1
            else:
                now.next = ListNode(val)
                carry = 0

            now = now.next

        if carry == 1:
            now.next = ListNode(1)

        return first.next
