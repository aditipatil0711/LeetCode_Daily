class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 0;
        int  i = 0;
        int j = 1;

        for (i = 1; i<nums.length; i++){
            if(nums[i-1] != nums[i]){
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
        
    }
}