class Solution {
    boolean visited[][];
    public boolean exist(char[][] board, String word) {
        
        int rows = board.length;
        int columns = board[0].length;
        visited = new boolean[rows][columns];
        
        for(int i=0;i<rows;i++){
            for (int j=0;j<columns;j++){
                if(word.charAt(0)==board[i][j] && searchWord(i,j,0,board,word)){
                    return true;
                }
            }
        }
        
        return false;
    }
    public boolean searchWord(int i,int j,int index, char[][] board,String word){
        
        
        if(index==word.length()){
            return true;
        }
        if(i<0 || i>=board.length || j<0 || j>=board[i].length || word.charAt(index) != board[i][j] || visited[i][j]){
            return false;
        }
        visited[i][j]= true;
        if(
            searchWord(i+1,j,index+1,board,word) ||
            searchWord(i,j+1,index+1,board,word) ||
            searchWord(i-1,j,index+1,board,word) ||
            searchWord(i,j-1,index+1,board,word) 
        ){
            return true;
        }
        visited[i][j]= false;
        return false;
    }
    
}



# 79. Word Search
# Medium

# 15105

# 625

# Add to List

# Share
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
