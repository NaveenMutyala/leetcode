class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxRect(heights):
            mxArea = 0 
            stk = []
            for i,h in enumerate(heights):
                start = i
                while stk and stk[-1][1]> heights[i]:
                    ind, ht = stk.pop()
                    mxArea = max(mxArea,ht*(i-ind))
                    start = ind
                stk.append([start,h])
            for i,h in stk[::-1]:
                mxArea = max(mxArea,h*(len(heights)-i))
            return mxArea
        r = len(matrix)
        c = len(matrix[0])
        hts =[0]*c
        area = 0
        for i in range(r):
            for j in range(c):
                # print(matrix[i][j])
                if matrix[i][j]=='1':
                    hts[j]+=1
                else:
                    hts[j]=0
            # print(hts)
            temp = maxRect(hts)
            # print(temp)
            area = max(area,temp)
        return area

# 85. Maximal Rectangle
# Hard

# 10359

# 182

# Add to List

# Share
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = [["0"]]
# Output: 0
# Example 3:

# Input: matrix = [["1"]]
# Output: 1
