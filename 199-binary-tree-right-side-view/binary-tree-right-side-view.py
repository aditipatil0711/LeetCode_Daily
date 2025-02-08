# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        res =[]
        q = deque([root])

        while q:
            right =None

            for i in range(len(q)):
                node = q.popleft()

                right = node #Right most of this level
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(right.val)
        return res

        

   
