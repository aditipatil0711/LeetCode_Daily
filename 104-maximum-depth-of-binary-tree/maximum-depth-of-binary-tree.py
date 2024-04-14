# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node,depth):
            if node is None:
                return
            depth +=1
            traverse(node.left,depth)
            traverse(node.right,depth)

            if node.left is None and node.right is None:
                self.res = max(depth,self.res)
        
        depth =0
        self.res = 0
        traverse(root,depth)
        return self.res