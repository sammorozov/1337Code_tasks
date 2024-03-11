from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        

        '''
        the rule:

        row_ones[i] + col_ones[j] - row_zeroz[i] - col_zeroz[j]

        this is the result of new_grid[i][j] 

        '''
        t_grid = list(zip(*grid))

        new_grid = [[0 for i in range(len(grid[0]))] for _ in range(len(grid))]


        for i in range(len(grid)):
            row_ones_i = grid[i].count(1)
            row_zeroz_i = grid[i].count(0)

            for j in range(len(grid[0])):

                
                col_ones_j = t_grid[j].count(1)
                col_zeroz_j = t_grid[j].count(0)

                new_grid[i][j] = row_ones_i + col_ones_j - row_zeroz_i - col_zeroz_j

        return new_grid

    
'''

CHAT GPT SOLUTION

from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        row_ones = [0] * rows
        row_zeros = [0] * rows

        col_ones = [0] * cols
        col_zeros = [0] * cols

        # Calculate row and column counts
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_ones[i] += 1
                    col_ones[j] += 1
                else:
                    row_zeros[i] += 1
                    col_zeros[j] += 1

        # Calculate the difference matrix
        diff = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                diff[i][j] = row_ones[i] + col_ones[j] - row_zeros[i] - col_zeros[j]

        return diff

# Test the function
grid = [
    [0, 1, 1],
    [1, 0, 1],
    [0, 0, 1]
]

sol = Solution()
result = sol.onesMinusZeros(grid)
print(result)  # Output the difference matrix


'''