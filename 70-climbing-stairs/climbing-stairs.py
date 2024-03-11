class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        f,s = 1,2
        if n==1:
            return 1
        for i in range(2,n):
            temp = f+s
            f = s
            s = temp
        return s

        