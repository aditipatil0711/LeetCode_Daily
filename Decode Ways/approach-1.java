class Solution {

     Map<Integer,Integer> memo = new HashMap<>();
    public int numDecodings(String s) {
       return recursivememo(0,s);

    }

    public int recursivememo(int index, String s){
        if(memo.containsKey(index)){
            return memo.get(index);
        }
        
        if (index == s.length()){
            return 1;
        }

        if(s.charAt(index) == '0'){
            return 0;
        }

        if (index == s.length()-1){
            return 1;
        }

        int ans = recursivememo(index+1,s);
        if(Integer.parseInt(s.substring(index,index+2))<=26){
            ans += recursivememo(index+2,s);
        }
        memo.put(index,ans);
        return ans;
        
        
    }

}
