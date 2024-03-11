from typing import *

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return list(set(edges[0]) & set(edges[1]))[0]





























