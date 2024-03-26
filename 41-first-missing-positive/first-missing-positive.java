class Solution {
    // TC : O(N) & SC : O(1)
    // N -> Length of the array 'nums'
    public int firstMissingPositive(int[] nums) {
        // Write your code here
        // Iterate through the array 'nums'
        for (int i = 0; i < nums.length; i++) {
            // Replace negative numbers with '0'
            // This is to ensure that only positive numbers are considered
            if (nums[i] < 0) {
                nums[i] = 0;
            }
        }
        // Traverse the array 'nums' again
        for (int i = 0; i < nums.length; i++) {
            // Mark elements by negating the value at their respective index minus one
            int index = Math.abs(nums[i]) - 1;
            // If 'nums[nums[i] - 1]' is positive
            if (index >= 0 && index < nums.length && nums[index] > 0) {
                // Mark 'nums[nums[i] - 1]' as negative
                nums[index] = nums[index] * (-1);
            }
            // If 'nums[nums[i] - 1]' is 0
            if (index >= 0 && index < nums.length && nums[index] == 0) {
                // We mark it with a special negative value '(nums.length + 1) * (-1)'
                // To differentiate it from other negative numbers
                nums[index] = (nums.length + 1) * (-1);
            }
            // If 'nums[nums[i] - 1]' is already negative
            // It means the number 'nums[i]' has been encountered before
            // So we don't need to mark it again
        }
        // Iterate through the modified array 'nums'
        for (int i = 1; i <= nums.length; i++) {
            // The first index 'i' with a positive number indicates the absence of the positive integer '(i + 1)'
            int index = i - 1;
            if (nums[index] >= 0) {
                // Return '(i + 1)' as the first missing positive
                int firstMissingPositiveNumber = i;
                return firstMissingPositiveNumber;
            }
        }
        // If no such index is found
        // Return '(nums.length + 1)' as the first missing positive
        int firstMissingPositiveNumber = nums.length + 1;
        return firstMissingPositiveNumber;
    }
}