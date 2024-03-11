from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(x, y): 
            while(y):
                x, y = y, x % y
            return x  

        if not head or not head.next:
            return head  

        current = head

        while current.next:
            common_divisor = gcd(current.val, current.next.val)
            new_node = ListNode(common_divisor, current.next)
            current.next = new_node
            current = new_node.next  # Move to the next original node

        return head


        


