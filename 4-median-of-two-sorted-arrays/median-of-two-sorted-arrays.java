class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
         // Ensure nums1 is the smaller array
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.length;
        int n = nums2.length;

        int low = 0, high = m;

        while (low <= high) {
            // Partition nums1
            int partitionX = (low + high) / 2;
            // Partition nums2 such that left + right are balanced
            int partitionY = (m + n + 1) / 2 - partitionX;

            // Handle edge cases with Integer.MIN_VALUE / MAX_VALUE
            int maxLeftX = (partitionX == 0) ? Integer.MIN_VALUE : nums1[partitionX - 1];
            int minRightX = (partitionX == m) ? Integer.MAX_VALUE : nums1[partitionX];

            int maxLeftY = (partitionY == 0) ? Integer.MIN_VALUE : nums2[partitionY - 1];
            int minRightY = (partitionY == n) ? Integer.MAX_VALUE : nums2[partitionY];

            // Check if partition is valid
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // Even total length
                if ((m + n) % 2 == 0) {
                    return ((double)Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
                } else {
                    // Odd total length, return max of left side
                    return (double)Math.max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                // Move partitionX left
                high = partitionX - 1;
            } else {
                // Move partitionX right
                low = partitionX + 1;
            }
        }
         throw new IllegalArgumentException("Input arrays are not sorted or not valid.");
    }
    
}