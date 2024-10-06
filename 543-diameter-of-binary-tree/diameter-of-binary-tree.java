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
    public int maxD = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        

        maxDepth(root);

        return maxD;

    }

    public int maxDepth(TreeNode root){
         if (root == null){
            return 0;
        }
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);

        maxD = Math.max(maxD,leftDepth+rightDepth);

        return Math.max(leftDepth,rightDepth)+1;
    }
}