from typing import *

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        out = []

        s = '123456789'

        left = 0
        right = 1

        while (left < len(s)):

            temp = s[left:right]

            if (int(temp) >= low) and (int(temp) <= high):
                out.append(int(temp))

            if right != len(s):
                right += 1
            else:
                left += 1
                right = left + 1

        return sorted(out)

            
print(Solution().sequentialDigits(low = 1000, high = 13000))