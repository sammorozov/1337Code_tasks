# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import *
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        new = fast = slow = ListNode('sentiel', head)
        for _ in range(n):
            fast = fast.next

        while fast.next != None:
            slow, fast = slow.next, fast.next

        
        slow.next = slow.next.next


        return new.next


            


