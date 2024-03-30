class Solution {
    public boolean isValid(String str) {
        Stack<Character> stack = new Stack<>();
        char ch;
        char[] arr = str.toCharArray();

        for(int i = 0; i<str.length();i++){
            ch = arr[i];
            if(ch=='(' || ch == '[' || ch =='{'){
                stack.push(ch);
                continue;
            }

            if(stack.empty()) return false;
            if(ch == ')' && stack.pop() != '(') return false;
            if(ch == '}' && stack.pop() != '{') return false;
            if(ch == ']' && stack.pop() != '[') return false;

        }
        if(!stack.empty()) return false;
        return true;
    }
}