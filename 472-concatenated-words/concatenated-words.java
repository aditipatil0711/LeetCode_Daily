class Solution {
    Set<String> wordSet;
    Map<String, Boolean> memo;
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        wordSet = new HashSet<>(Arrays.asList(words));
        memo = new HashMap<>();
        List<String> ans = new ArrayList<>();

        for(String word: words){
            if(wordSet.isEmpty()) continue;
            wordSet.remove(word);
            if(canForm(word)) ans.add(word);
            wordSet.add(word);
        }

        return ans;

    }

    private boolean canForm(String word){
        if(memo.containsKey(word)){
            return memo.get(word);
        }

        for(int i = 1; i<word.length(); i++){
            String left = word.substring(0,i);
            String right = word.substring(i);

            if(wordSet.contains(left)){
                if(wordSet.contains(right)||canForm(right)){
                    memo.put(word, true);
                    return true;
                }
            }
        }
        memo.put(word, false);
        return false;
        
    }
}