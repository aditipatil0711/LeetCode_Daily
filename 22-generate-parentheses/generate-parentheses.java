class Solution {
    public List<String> generateParenthesis(int n) {

        List<String> ans = new ArrayList<>();

        backtracking(ans,new StringBuilder(), 0,0,n);

        return ans;   
    }

    public void backtracking(List<String> ans, StringBuilder sb, int left, int right, int n ){

        if(sb.length() == 2*n){
            ans.add(sb.toString());
        }
        if(left<n){
            sb.append("(");
            backtracking(ans, sb, left +1,right,n);
            sb.deleteCharAt(sb.length() - 1);
        }
        if(left>right){
            sb.append(")");
            backtracking(ans, sb, left,right+1,n);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}