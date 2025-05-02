class Solution {
    public int trap(int[] height) {
        int i = 0;
        int j = height.length - 1;

        int lh = height[i];
        int rh = height[j];
        int total = 0;

        while(i<j){
            if (lh < rh){
                i++;
                lh = Math.max(lh, height[i]);
                total += (lh - height[i]);
            }
            else{
                j--;
                rh = Math.max(rh, height[j]);
                total += (rh -height[j]); 
            }
        }

        return total;
        
    }
}