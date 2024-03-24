public class Solution {
    public int findDuplicate(int[] nums) {
        // Initialize slow and fast pointers
        int slow = nums[0];
        int fast = nums[0];

        // Move slow one step and fast two steps at a time
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        // Reset one pointer to the start and find the meeting point
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }

        // Return the repeated number (meeting point)
        return slow;
    }
}