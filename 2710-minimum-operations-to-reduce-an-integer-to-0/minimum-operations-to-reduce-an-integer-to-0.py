class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)
        co=0
        res = 0

        while n>0:
            if n&1 == 1:
                co+=1
            elif co>0:
                res +=1
                co = 0 if co==1 else 1
            n>>=1
        if co==1:
            res +=1
        elif co> 1:
            res +=2
        return res




        