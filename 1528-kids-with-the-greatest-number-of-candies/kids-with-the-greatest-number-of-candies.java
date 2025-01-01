class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        //find greatest number
        int maxCandies = 0;
        for ( int c : candies){
            maxCandies = Math.max(c,maxCandies);
        }
        //for loop madhe compare and result array madhe add karne
        List<Boolean> result = new ArrayList<>();
        for (int c : candies){
            result.add(c + extraCandies >= maxCandies);
        }
        return result;
    }
}