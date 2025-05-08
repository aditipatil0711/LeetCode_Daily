class TrieNode{
    TrieNode[] children = new TrieNode[26];
    String word = null;
}



class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        int m = board.length;
        int n = board[0].length;

        List<String> ans = new ArrayList<>();
        TrieNode tree = buildTree(words);

        for(int i = 0; i<m; i++){
            for(int j = 0; j < n; j++){
                dfs(i,j,board, tree, ans);
            }
        }

        return ans;
        
    }

    private TrieNode buildTree(String[] words){
        TrieNode root = new TrieNode();
        for(String word: words){
            TrieNode node = root;
            for(char ch: word.toCharArray()){
                int index = ch - 'a';
                if(node.children[index]==null){
                    node.children[index] = new TrieNode();
                }
                node = node.children[index];
            }
            node.word = word;
        }

        return root;
    }

    private void dfs(int i, int j, char[][] board, TrieNode node, List<String> ans){

        char ch = board[i][j];

        if (ch == '#' || node.children[ch - 'a'] == null) return;

        node = node.children[ch - 'a'];
        if(node.word !=  null){
            ans.add(node.word);
            node.word = null;
        }
        
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        board[i][j] = '#'; 

        for( int d = 0; d< 4; d++){
            int x = i + dx[d];
            int y = j + dy[d];
            if (x >= 0 && y >= 0 && x < board.length && y < board[0].length) {
            dfs(x, y, board, node, ans);
        }

        }
         board[i][j] = ch;

    }
}