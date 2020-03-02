# https://leetcode.com/problems/unique-paths/
# Medium
# Notes: Did it in python this time. Kinda slow. Probably needs memoization


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * m] * n
        
        for row in range(n):
            for col in range(m):
                if row - 1 < 0 and col - 1 < 0:
                    grid[row][col] = 1
                elif row - 1 < 0:
                    grid[row][col] = grid[row][col - 1]
                elif col - 1 < 0:
                    grid[row][col] = grid[row - 1][col]
                else:
                    grid[row][col] = grid[row-1][col] + grid[row][col-1]
                #print(f'row:{row}, col:{col}, val:{grid[row][col]}')
                
        
        return grid[n-1][m-1]
    
                
                
            
        
        
        
            
                