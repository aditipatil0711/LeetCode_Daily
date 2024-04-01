# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def dfs(root,path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    res.append(path)
                else:
                    path += '->'
                    dfs(root.left,path)
                    dfs(root.right,path)

        dfs(root,'')
        return res
        