from typing import *

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        cnt = 0



        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:

                    k = j

                    row = [m for m in mat[i]]

                    col = [mat[i][k] for i in range(len(mat[i]))]

                    if (row).count(1) == 1 and (col).count(1) == 1:
                        cnt += 1

        return cnt
                    
print(Solution().numSpecial( mat = [[1,0,0],[0,1,0],[0,0,1]]))


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        ans=0
        transposeMat=list(zip(*mat))
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1 and sum(mat[i])==1 and sum(transposeMat[j])==1:
                    ans+=1
        return ans            
    

'''
транспонирование матрицы
        transposeMat=list(zip(*mat))

        как оно работает я хуй знает
'''