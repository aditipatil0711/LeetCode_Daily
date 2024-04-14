# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
            
        def dfs(root):
            if root is None:
                return 0
            lh = dfs(root.left)
            rh = dfs(root.right)
            if lh==-1 or rh==-1 or abs(lh-rh)>1:
                return -1
            else:
                return max(lh,rh)+1
        
        return dfs(root)!=-1
