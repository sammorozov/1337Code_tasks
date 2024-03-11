from typing import *

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        

        happiness.sort() 

        ans = 0
        for i in range(k):

            last = happiness.pop()

            try:
                happiness[-1] -= (i + 1)
            except:
                pass


            if last <= 0:
                continue

            else:
                ans += last

                

        return ans
    
print(Solution().maximumHappinessSum(happiness = [2,3,4,5], k = 3))