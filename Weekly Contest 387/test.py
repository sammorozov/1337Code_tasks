from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        R,C,answ=len(grid),len(grid[0]),0
        for r in range(R):
            rowSum=0
            for c in range(C):
                rowSum+=grid[r][c]
                grid[r][c]=rowSum
                if r:
                    grid[r][c]+=grid[r-1][c]
                if grid[r][c]<=k:
                    answ+=1
                else:
                    break
        return answ
print(Solution().countSubmatrices(grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20))