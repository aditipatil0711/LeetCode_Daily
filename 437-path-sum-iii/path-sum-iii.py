# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """

        def dfs_prefix_sum_traversal(node,curr,hashmap):
            if not node:
                return 0

            curr += node.val

            count = hashmap.get(curr-targetSum,0)

            hashmap[curr] = hashmap.get(curr,0)+1

            count +=dfs_prefix_sum_traversal(node.left,curr,hashmap)
            count +=dfs_prefix_sum_traversal(node.right,curr,hashmap)

            #Needed while moving up the tree to calculate other branches

            if hashmap[curr] ==1:
                del hashmap[curr]
            else:
                hashmap[curr] -=1

            return count




        hashmap = {0:1}

        return dfs_prefix_sum_traversal(root, 0, hashmap )
            

