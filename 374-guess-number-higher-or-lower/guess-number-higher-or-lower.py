# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        l = 1
        r = n
       

        while l<=r:
            mid = l + (r - l) // 2  # Ensure integer division
            if guess(mid)==0:
                return mid
            elif guess(mid) == -1:
                r = mid-1
            else:
                l = mid+1

        