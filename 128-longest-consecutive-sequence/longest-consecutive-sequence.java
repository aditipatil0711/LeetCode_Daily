class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        int max = 0;

        for(int i = 0; i<nums.length; i++){
            set.add(nums[i]);
        }

        for(int num:set){
            if (!set.contains(num-1)){
                int curr = num;
                int streak = 1;

                while(set.contains(curr+1)){
                    streak+=1;
                    curr+=1;
                }

                max = Math.max(streak, max);

            }

        }

        return max;
        
    }
}