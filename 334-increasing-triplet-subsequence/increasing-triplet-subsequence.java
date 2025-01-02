class Solution {
    public boolean increasingTriplet(int[] nums) {
        int fn = Integer.MAX_VALUE;
        int sn = Integer.MAX_VALUE;
        for (int i : nums){
            if(i<=fn){
                fn = i;
            }
            else if (i<=sn){
                sn=i;
            }
            else{
                return true;
            }
        }
        return false;
        
    }
}