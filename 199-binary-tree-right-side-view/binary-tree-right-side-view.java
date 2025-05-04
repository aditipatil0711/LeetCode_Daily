/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null){
            return new ArrayList<Integer>();
        }

        ArrayDeque<TreeNode> nextLevel = new ArrayDeque(){
            {
                offer(root);
            }
        };
        ArrayDeque<TreeNode> curr = new ArrayDeque();
        List<Integer> ans = new ArrayList();

        TreeNode node = null;
        while(!nextLevel.isEmpty()){
            curr = nextLevel;
            nextLevel = new ArrayDeque<>();

            while(!curr.isEmpty()){
                node = curr.poll();
                if(node.left != null){
                    nextLevel.offer(node.left);
                }
                if(node.right != null){
                    nextLevel.offer(node.right);
                }
            }
            ans.add(node.val);
        }
        return ans;
        
    }
}