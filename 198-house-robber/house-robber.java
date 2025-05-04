class Solution {
    public int rob(int[] nums) {

        int n = nums.length;

        int[] dp = new int[n];

        for(int i = 0; i<n; i++){
            dp[i] = -1;
        }
    
        return robOrNot(0,nums, dp);

        // rob(thisOne, nextOne)
        
    }

    public int robOrNot(int i, int[] nums, int[] dp ){
        if (i>=nums.length){
            return 0;
        }

        if(dp[i] != -1 ){
            return dp[i];
        }

        int thisOne = nums[i] + robOrNot(i+2, nums,dp);
        int nextOne = robOrNot(i+1, nums, dp);

        dp[i] = Math.max(thisOne, nextOne);

        return dp[i];
    }
}