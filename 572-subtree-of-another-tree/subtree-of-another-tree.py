# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if node is None:
                return False
            elif isIdentical(node,subRoot):
                return True
            return dfs(node.right) or dfs(node.left)
        def isIdentical(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return (node1.val == node2.val and 
                    isIdentical(node1.left, node2.left) and 
                    isIdentical(node1.right, node2.right))
        return dfs(root)


        