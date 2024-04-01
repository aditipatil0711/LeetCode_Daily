class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = s.split()
        print(ans)
        res = len(ans[-1])
        return res
        