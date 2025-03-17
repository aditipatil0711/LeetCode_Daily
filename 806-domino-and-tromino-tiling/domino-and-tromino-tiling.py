class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 1000000007

        if n <= 2:
            return n

        f = [0]*(n+1)
        p = [0]*(n+1)

        f[1] = 1
        f[2] = 2
        p[2] = 1
        
        for k in range(3, n + 1):
            f[k] = (f[k - 1] + f[k - 2] + 2 * p[k - 1]) % MOD
            p[k] = (p[k - 1] + f[k - 2]) % MOD
        return f[n]