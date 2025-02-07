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
        if not root:
            return 0
        
        stack = [(root,root.val)]
        goodnodes = 0

        while stack:
            node, max_so_far = stack.pop()

            if node.val >= max_so_far:
                goodnodes+=1
            
            max_new = max(max_so_far,node.val)

            if node.right:
                stack.append((node.right,max_new))
            if node.left:
                stack.append((node.left,max_new))

        return goodnodes





        