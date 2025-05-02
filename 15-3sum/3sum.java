class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> ans = new HashSet<>();
        Arrays.sort(nums); 
        for(int i =0; i<nums.length-2; i++){
            // Skip duplicate i's
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int target = -nums[i];
            List<List<Integer>> pairs = twoSum(nums, i + 1, target);

            for (List<Integer> pair : pairs) {
                List<Integer> triplet = Arrays.asList(nums[i], pair.get(0), pair.get(1));
                ans.add(triplet);  // Set avoids duplicates
            }
        }

        return new ArrayList<>(ans);
        
    }

    public List<List<Integer>> twoSum(int[] nums, int start, int target){
        Set<Integer> set = new HashSet<>();
        Set<List<Integer>> pairs = new HashSet<>();

        for(int i = start; i<nums.length; i++){
            int comp = target - nums[i];
            if (set.contains(comp)){
                List<Integer> pair = Arrays.asList(comp, nums[i]);
                Collections.sort(pair);
                pairs.add(pair);
            }
            set.add(nums[i]);
        }

        return new ArrayList<>(pairs);

    }

    


   
}