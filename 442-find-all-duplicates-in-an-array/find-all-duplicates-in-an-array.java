class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> arrayList = new ArrayList<>();
        // because we know the element only appear onece
        // or twice, if this element appear twice, their
        // correponding index will be access twic, but since
        // integers are limit [1 to n] so we need to set it is
        // nums[corresponding index - 1] become negative
        for (int i = 0; i < nums.length; i += 1) {
            if (nums[Math.abs(nums[i]) - 1] < 0) {
                arrayList.add(Math.abs(nums[i]));
            }
            nums[Math.abs(nums[i]) - 1] *= -1;
        }
        return arrayList;
    }
}