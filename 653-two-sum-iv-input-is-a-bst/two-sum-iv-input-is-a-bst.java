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
    public boolean findTarget(TreeNode root, int k) {
        Set<Integer> seen = new HashSet<>();
        return dfs(seen, root, k);
    }
    private boolean dfs(Set<Integer> seen, TreeNode root, int k){
        if(root == null) return false;

        if(seen.contains(k-root.val)) return true;

        seen.add(root.val);

        return dfs(seen,root.left,k) || dfs(seen,root.right,k);
    }
}