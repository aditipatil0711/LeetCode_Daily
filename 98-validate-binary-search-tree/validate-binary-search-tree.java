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
    public boolean isValidBST(TreeNode root) {
        return helper(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public boolean helper(TreeNode root, long minv, long maxv){
        if(root == null){
            return true;
        }

        if (root.val <= minv || root.val >= maxv){
            return false;
        }

        boolean left = helper(root.left, minv, root.val);
        boolean right = helper(root.right, root.val, maxv);

        return left && right;
    }
}