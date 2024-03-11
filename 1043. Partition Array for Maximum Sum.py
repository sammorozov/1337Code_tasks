from typing import *

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        D = [0] * len(arr)
        for idx in range(len(arr)):
            m,d = -float('inf'), -float('inf')

            for jdx in range(0, min(k, idx+1)):
                m = max(arr[idx - jdx], m)
                d = max(d, m*(jdx + 1) + D[-jdx-1])
            
            D = D[1:] + [d]

        return D[-1]


