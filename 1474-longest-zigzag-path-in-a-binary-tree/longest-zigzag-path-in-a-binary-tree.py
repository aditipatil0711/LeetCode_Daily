# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.length = 0

        #leftOrRight = true -> Left else go Right (leftOrRight=False)


        def dfs(node, leftOrRight, steps):
            if node: #(not node-> Exit )
                self.length = max(self.length,steps)

                if leftOrRight:
                    dfs(node.left,False,steps+1)
                    dfs(node.right,True,1)
                else:
                    dfs(node.left,False,1)
                    dfs(node.right,True, steps+1)

        dfs(root,True,0)
        return self.length


        