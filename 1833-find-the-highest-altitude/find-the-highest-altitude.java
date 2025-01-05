class Solution {
    public int largestAltitude(int[] gain) {
        int maxAlt = 0;
        int total = 0;

        for (int i = 0; i<gain.length; i++){
            total += gain[i];
            maxAlt = Math.max(total, maxAlt);
        }
        return maxAlt;
    }
}