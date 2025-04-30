class Solution {
    public String removeDuplicates(String s, int k) {
        StringBuilder sb = new StringBuilder();
        Stack<Integer> countStack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            sb.append(c);

            
            if (sb.length() >= 2 && sb.charAt(sb.length() - 1) == sb.charAt(sb.length() - 2)) {
                int count = countStack.pop() + 1;
                

                if (count == k) {
                    sb.delete(sb.length() - k, sb.length());
            
                } else {
                    countStack.push(count);
                }
            } else {
                countStack.push(1);
                System.out.println("New char, pushed 1 to countStack");
            }

        }

        return sb.toString();
    }
}
