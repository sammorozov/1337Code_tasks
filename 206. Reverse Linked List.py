# Definition for singly-linked list.

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        r_list = []

        for i in range(len(head)-1, -1, -1):

            value = head[i].val

            temp = ListNode(value)

            r_list.append(temp)

        for j in range(len(r_list)-1):

            r_list[j].next = r_list[i+1]
        
        return r_list
    

    
def print_linked_list(head: Optional[ListNode]) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next

    print("None")

mytest = [1, 2, 3, 42]
nodes = []

for i in mytest:
    temp = ListNode(i)
    nodes.append(temp)

for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

print_linked_list(Solution().reverseList(nodes))
     





'''
chat solution

# Definition for singly-linked list.
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

def print_linked_list(head: Optional[ListNode]) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

mytest = [1, 2, 3, 42]
nodes = None
for i in mytest[::-1]:  # Reverse the list to build the linked list in the correct order
    temp = ListNode(i, nodes)
    nodes = temp

print_linked_list(Solution().reverseList(nodes))


'''