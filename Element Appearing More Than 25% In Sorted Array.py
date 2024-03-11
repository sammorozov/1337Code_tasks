from typing import *

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        if len(arr) == 1:
            return arr[0]
        
        cnt = 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                cnt += 1

                if (cnt+1)/len(arr) > 0.25:
                    return arr[i]
                
            else:
                cnt = 0

print(Solution().findSpecialInteger(arr = [1,2,3,3]))