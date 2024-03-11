from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        temp = ListNode()
        current = temp

        
        t_str_1 = ''
        t_str_2 = ''

        while l1:
            t_str_1 += str(l1.val)
            l1 = l1.next


        while l2:
            t_str_2 += str(l2.val)
            l2 = l2.next



        out = str(int(t_str_1[::-1]) + int(t_str_2[::-1]))

        for i in range(len(out)-1, -1, -1):
            current.val = int(out[i])
            if i != 0:            
                current.next = ListNode()
                current = current.next


        return temp
    

        

