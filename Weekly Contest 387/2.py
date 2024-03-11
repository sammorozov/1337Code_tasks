from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        

        def list_pull(L, result_list=None):
            if result_list is None:
                result_list = []

            for i in L:
                if type(i) == list:
                    list_pull(i, result_list)
                else:
                    result_list.append(i)

            return result_list

        n = len(grid)
        m = len(grid[0])

        cnt = 0
        def gen_comb(n, m):
            some_comb = []

            for i in range(1, n+1):
                for j in range(1, m+1):
                    
                    if i + j <= max(n, m) + 1:


                        some_comb.append((i , j))


            return some_comb
        

        my_comb = gen_comb(n, m)

        # print(my_comb)
        for comb in my_comb:
            a, b = comb[0], comb[1]
            

            somestr = [j[:b] for j in [grid[i] for i in range(len(grid)) if i < a]]
            # print(somestr)

            temp_s = sum(list_pull(somestr))
            
            if temp_s <= k:
                cnt += 1



        return cnt
    

print(Solution().countSubmatrices([[3,10,5],[6,3,1]], 4))