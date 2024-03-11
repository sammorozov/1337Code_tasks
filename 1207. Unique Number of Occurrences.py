from collections import Counter
from typing import *

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(Counter(arr).values()) == len(set(Counter(arr).values()))
    

print(Solution().uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))

