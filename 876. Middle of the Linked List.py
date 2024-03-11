from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


mytest = [1, 2, 3, 4, 5,888,1, 12,2,2]
nodes = []

for i in mytest:
    temp = ListNode(i)
    nodes.append(temp)

for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

    #print(nodes[i], nodes[i].next, nodes[i+1])


class Solution:
    def len_list(self, head: Optional[ListNode]) -> int:
        len_ll = 0
        while head:
            len_ll += 1
            head = head.next

        return len_ll
    

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        len_list = self.len_list(head)
        mid_ind = len_list // 2 + 1
        cnt = 1

        while head:
            if cnt == mid_ind:
                return head
            else:
                cnt += 1
                head = head.next



def print_linked_list(head: Optional[ListNode]) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

print_linked_list(Solution().middleNode(nodes[0]))

    
