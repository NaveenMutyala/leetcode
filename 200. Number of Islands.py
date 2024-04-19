class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        r = len(grid)
        c = len(grid[0])
        def dfs(i,j):
            if (i<0 or j<0 or i>=r or j>=c or grid[i][j]!='1'):
                return 
            grid[i][j] ='0'
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
            
        no_of_islands = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1':
                    no_of_islands +=1
                    dfs(i,j)

        return no_of_islands


# 200. Number of Islands
# Medium

# 22217

# 497

# Add to List

# Share
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
