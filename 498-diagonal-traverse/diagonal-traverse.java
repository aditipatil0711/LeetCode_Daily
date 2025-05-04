class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int R = mat.length;
        int C = mat[0].length;
        boolean goingup = true;
        int[] ans = new int[R*C];
        int i = 0;
        int j = 0;
        int k = 0;

      
        while(k< R*C){
            ans[k] = mat[i][j];
            k++;
            if(goingup == true){
                if(j == C-1){
                    i++;
                    goingup = false;
                }
                else if(i==0){
                    j++;
                    goingup = false;
                }
                else{
                    i--;
                    j++;
                }

            }
            else{
                if(i == R-1){
                    j++;
                    goingup = true;
                }
                else if(j==0){
                    i++;
                    goingup = true;
                }
                
                else{
                    i++;
                    j--;
                }

            }
        }

        return ans;
        
    }
}