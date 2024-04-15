# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0

        def dfs(root,max_val):
            if not root:
                return 0
            is_good = 1 if max_val <= root.val else 0
            max_val = max(max_val,root.val)

            lg = dfs(root.left,max_val)
            rg = dfs(root.right,max_val)

            return is_good + lg + rg
        return dfs(root,root.val)