class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        perimeter = 0
        for i in range(r):
            for j in range(c):
                temp =4
                if grid[i][j]==1:
                    if i-1 >=0 or j-1>=0:
                        if i>0 and grid[i-1][j]==1:
                            temp-=1
                        if j>0 and grid[i][j-1]==1:
                            temp=temp-1
                    if i+1<r or j+1<c:
                        if i+1<r and grid[i+1][j]==1:
                            temp-=1
                        if j+1<c and grid[i][j+1]==1:
                            temp -=1
                    perimeter+=temp
        return perimeter



# 463. Island Perimeter
# Easy

# 6356

# 339

# Add to List

# Share
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4
 

# Constraints:

# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.
