# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        return self.getLeafNodes(root1) == self.getLeafNodes(root2)

    def getLeafNodes(self,root):
        if not root:
            return []
        
        leaf_values = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node.left is None and node.right is None:
                leaf_values.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return leaf_values
        