class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();

        if(matrix == null|| matrix.length ==0) return result;

        int m = matrix.length;
        int n = matrix[0].length;
        int[][] directions = {{0,1},{1,0},{0,-1},{-1,0}};
        int dir = 0;
        boolean visited[][]  = new boolean[m][n];
        visited[0][0] = true;
        int row = 0;
        int col = 0;
        for(int i = 0; i<m*n; i++){
            result.add(matrix[row][col]);
            visited[row][col] = true;

            int nextRow = row + directions[dir][0];
            int nextCol = col +directions[dir][1];

            if(nextRow >= 0 && nextRow < m && nextCol >= 0 && nextCol < n && !visited[nextRow][nextCol]){
                row = nextRow;
                col = nextCol;
            }
            else{
                dir = (dir + 1) % 4;
                row += directions[dir][0];
                col += directions[dir][1];
            }
    
        }

        return result;
    }
}