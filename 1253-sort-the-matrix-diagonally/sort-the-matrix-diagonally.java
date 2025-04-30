class Solution {
    public int[][] diagonalSort(int[][] mat) {
        int R = mat.length;
        int C = mat[0].length;
      


        for (int row = R - 1; row >= 0; row--){
            List<Integer> temp = new ArrayList<>();
            int r = row;
            int c = 0;
            while(r<R  && c< C){
                temp.add(mat[r][c]);
                r++;
                c++;
            }
            Collections.sort(temp);
            r = row; c = 0;
            int i = 0;
            while(r<R  && c< C){
                mat[r][c] = temp.get(i);
                i++;
                r++;
                c++;
            }
        
        }

        for (int col = 0; col < C; col++){
            List<Integer> temp = new ArrayList<>();
            int r = 0;
            int c = col;
            while(r<R  && c< C){
                temp.add(mat[r][c]);
                r++;
                c++;
            }
            Collections.sort(temp);
            r = 0; c = col;
            int i = 0;
            while(r<R  && c< C){
                mat[r][c] = temp.get(i);
                i++;
                r++;
                c++;
            }
        
        }

        return mat;
    }
}