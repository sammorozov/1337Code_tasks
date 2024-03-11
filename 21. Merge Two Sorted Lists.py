
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1  
                list1 = list1.next    
            else:
                current.next = list2  
                list2 = list2.next    
            current = current.next   

        
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next  






def print_linked_list(head: Optional[ListNode]) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")



mytest1 = [1, 2, 3, 4, 5]
nodes1 = []

for i in mytest1:
    temp = ListNode(i)
    nodes1.append(temp)

for i in range(len(nodes1) - 1):
    nodes1[i].next = nodes1[i + 1]

mytest2 = [1, 2, 9, 11, 15]
nodes2 = []

for i in mytest2:
    temp = ListNode(i)
    nodes2.append(temp)

for i in range(len(nodes2) - 1):
    nodes2[i].next = nodes2[i + 1]


print_linked_list(Solution().mergeTwoLists(nodes1[0], nodes2[0]))