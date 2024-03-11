from typing import *


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        our_len = len(capacity)
        capacity.sort(reverse=True)

        sum_appl = sum(apple)

        while sum_appl > 0:
            sum_appl -= capacity[0]
            del capacity[0]

        return our_len - len(capacity)
    

print(Solution().minimumBoxes( apple = [1,3,2], capacity = [4,3,1,5,2]))


