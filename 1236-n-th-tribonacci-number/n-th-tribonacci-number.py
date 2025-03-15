class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {0:0,1:1,2:1}
        def trib(i):
            if i in dp:
                return dp[i]
            dp[i] = trib(i-1)+trib(i-2)+trib(i-3)
            return dp[i]
        
        return trib(n)
        
        