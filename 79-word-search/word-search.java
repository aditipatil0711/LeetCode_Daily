class Solution {
    public boolean exist(char[][] board, String word) {
        int ROWS = board.length;
        int COLS = board[0].length;

        boolean[][] visited = new boolean[ROWS][COLS];

        for(int i = 0; i< ROWS; i++){
            for (int j = 0; j<COLS;j++){
                if(DFS(board, word, i, j, 0, visited)){
                return true;
            }
        }

        
    }
    return false;
    
    }


    public boolean DFS(char[][] board, String word, int i, int j, int k, boolean[][] visited){
        if(k==word.length()){
            return true;
        }

        if(i<0 ||j<0|| i>= board.length || j >= board[0].length || word.charAt(k)!=board[i][j]||visited[i][j]==true){
            return false;
        }
        
        visited[i][j] = true;

        boolean found = DFS(board, word, i+1, j, k+1, visited)||
                        DFS(board, word, i-1, j, k+1, visited)||
                        DFS(board, word, i, j+1, k+1, visited)||
                        DFS(board, word, i, j-1, k+1, visited);
        
        visited[i][j] = false;

        return found;

    }
}