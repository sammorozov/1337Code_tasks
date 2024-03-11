from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


mytest = [1, 2, 3, 4, 5]
nodes = []

for i in mytest:
    temp = ListNode(i)
    nodes.append(temp)

for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

    #print(nodes[i], nodes[i].next, nodes[i+1])


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = 0
        while head: 
            answer = 2*answer + head.val 
            head = head.next 
        return answer 
    
print(Solution().getDecimalValue(nodes[0]))