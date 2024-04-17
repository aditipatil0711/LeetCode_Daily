# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        smallest_string = [float('inf')]  # Use a list to hold the smallest string because lists are mutable.

        def dfs(node, current_string):
            if not node:
                return
            
            # Prepend the current character to the path string
            current_string = chr(node.val + ord('a')) + current_string

            # Check if the current node is a leaf
            if not node.left and not node.right:
                if smallest_string[0] == float('inf') or current_string < smallest_string[0]:
                    smallest_string[0] = current_string
                return

            # Continue DFS on the children
            if node.left:
                dfs(node.left, current_string)
            if node.right:
                dfs(node.right, current_string)

        dfs(root, "")
        return smallest_string[0] if smallest_string[0] != float('inf') else ""