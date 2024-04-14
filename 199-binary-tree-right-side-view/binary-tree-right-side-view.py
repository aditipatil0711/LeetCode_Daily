# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        

        def dfs(root,depth,result):
            if root is None:
                return None
            if depth == len(result):
                result.append(root.val)
            dfs(root.right,depth+1,result)
            dfs(root.left,depth+1,result)
        result = []
        depth = 0
        dfs(root,depth,result)
        return result