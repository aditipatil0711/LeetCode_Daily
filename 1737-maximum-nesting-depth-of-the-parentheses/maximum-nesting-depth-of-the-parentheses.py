class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        max_Depth = 0
        bracket = 0
        for c in s:
            if c == '(':
                bracket +=1
            elif c == ')':
                bracket -=1
            
            max_Depth = max(max_Depth,bracket)
        
        return max_Depth