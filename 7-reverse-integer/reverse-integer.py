class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = True if x<0 else False

        if is_negative == True:
            x = x*-1

        rev = 0

        while x>0:
            if rev > (2 ** 31 - 1) / 10 or rev < -2 ** 31 / 10:
                return 0
            rev = rev*10 + x%10
            x = x//10
        
        if is_negative==True:
            return rev*-1

         
        return rev
        