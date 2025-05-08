class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        List<String> ans = new ArrayList<>();

        backtrack(s, wordSet, new StringBuilder(), ans, 0);
        return ans;
    }

    private void backtrack(String s, Set<String> wordSet, StringBuilder sb, List<String>  ans, int i){
        if(i == s.length()){
            ans.add(sb.toString().trim());
            return;
        }

        for( int j = i+1; j<=s.length(); j++){
            String word = s.substring(i,j);
            if(wordSet.contains(word)){
                int currLength = sb.length();
                sb.append(word).append(" ");
                backtrack(s, wordSet, sb, ans, j);
                sb.setLength(currLength);
            }
        }
    }
}