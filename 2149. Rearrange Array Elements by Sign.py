from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        plus = []
        minus = []
        out = []
        for i in nums:
            if i < 0:
                minus.append(i)
            else:
                plus.append(i)

        for k, j in zip(plus, minus):
            out.append(k)
            out.append(j)

        return out 