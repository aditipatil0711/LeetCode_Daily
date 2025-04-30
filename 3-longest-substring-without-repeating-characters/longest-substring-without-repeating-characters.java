class Solution {
    public int lengthOfLongestSubstring(String s) {
        int count = 0;
        int l = 0;
        int r = 0;
        Map<Character, Integer> map = new HashMap<>();

        for( r = 0; r<s.length(); r++){

            char ch = s.charAt(r);
            if(map.containsKey(ch) && map.get(ch) >= l){
                l = map.get(ch)+1;
            }

            map.put(ch,r);

            count = Math.max(count, r-l+1);

        }

        return count;

        
    }
}