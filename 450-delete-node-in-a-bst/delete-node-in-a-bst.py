# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """

        if root is None: 
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left =  self.deleteNode(root.left,key)      
        else:
            if root.left == None and root.right == None:
                return None
        
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            successor = self.finInOrderNextVal(root.right)
            root.val = successor.val  
            root.right = self.deleteNode(root.right, successor.val)
        return root

    def finInOrderNextVal(self,root):
        while root.left:
            root = root.left
        return root
