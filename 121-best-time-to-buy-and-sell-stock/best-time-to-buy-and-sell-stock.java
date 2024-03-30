class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 0;
        int maxp = 0;

        while (r<prices.length){
            if (prices[l]<prices[r]){
                int diff = prices[r]-prices[l];
                maxp = Math.max(diff,maxp);
            }
            else{
                l = r;
            }
            r++;
        }

        return maxp;

    }
}