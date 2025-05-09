class Solution {
    public void moveZeroes(int[] nums) {
        int start = 0;
        int end = 0;

        while(end < nums.length){
            if(nums[end] == 0){
                end++;
            } else{
                int temp = nums[end];
                nums[end] = nums[start];
                nums[start] = temp;
                start++;
                end++;
            }
        }
        
    }
}