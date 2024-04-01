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
        def dfs(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:  # if reach a leaf
                    paths.append(path)  # update paths 
                else:
                    path += '->'  # extend the current path
                    dfs(node.left, path)
                    dfs(node.right, path)

        paths = []
        dfs(root, '')
        return paths