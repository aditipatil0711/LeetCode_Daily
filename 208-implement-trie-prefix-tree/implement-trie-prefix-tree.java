class TrieNode{
    Map<Character,TrieNode> children;
    boolean isEndOfWord;

    public TrieNode(){
        children = new HashMap<>();
        isEndOfWord = false;
    }
}

class Trie {
    TrieNode root;
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode current = root;
        for (char ch: word.toCharArray()){
            current = current.children.computeIfAbsent(ch, c-> new TrieNode());
        }
        current.isEndOfWord = true;
    }
    
    public boolean search(String word) {
        TrieNode current = root;
        for(char ch: word.toCharArray()){
            current = current.children.get(ch);
            if(current == null){
                return false;
            }
        }
        return current.isEndOfWord;
    }
    
    public boolean startsWith(String prefix) {
       TrieNode current = root;

        for(char c : prefix.toCharArray()) {
            if(current.children.containsKey(c)) {
                current = current.children.get(c);
            } else {
                return false;
            }
        }
        return true;
    
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */