class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
      int n = spells.length, m = potions.length;
        int[] result = new int[n];

        // Step 1: Sort the potions array
        Arrays.sort(potions);

        // Step 2: Iterate over each spell and use binary search to count successful pairs
        for (int i = 0; i < n; i++) {
            int spell = spells[i];
            int index = binarySearch(potions, spell, success);
            result[i] = m - index; // Count of successful potions
        }

        return result;
    }

    // Binary search to find the first valid potion
    private int binarySearch(int[] potions, int spell, long success) {
        int left = 0, right = potions.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            long product = (long) spell * potions[mid]; // Avoid integer overflow
            
            if (product >= success) {
                right = mid - 1; // Look for smaller valid potions
            } else {
                left = mid + 1; // Increase potion strength
            }
        }
        return left; // First valid potion index
    }


}