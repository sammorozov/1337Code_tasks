from typing import *

class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        s = s.strip().split()


        left = 0

        right = len(s) - 1

        while left < right:

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return ' '.join(s)


print(Solution().reverseWords(s = "the sky is blue"))
print(Solution().reverseWords(s = "  hello world  "))
print(Solution().reverseWords(s = "a good   example"))
