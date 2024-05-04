class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x
        l = 2
        r= x//2
        

        while l<=r:
            p = l + (r-l)//2
            num = p*p
            if num>x:
                r = p-1
            elif num<x:
                l=p+1
            else:
                return p
        return r
        
        