from collections import defaultdict
from typing import *

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        

        adj_list = defaultdict(list)

        for u, v in edges:

            adj_list[u].append(v)

            adj_list[v].append(u)
            
        seen = set()

        def dfs(node):

            if node == destination:
                return True

            seen.add(node)
            for v in adj_list[node]:
                if v not in seen and dfs(v):
                    return True
                
            return False

        return dfs(source)