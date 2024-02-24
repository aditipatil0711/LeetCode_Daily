class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = list(sorted(s))
        s2 = list(sorted(t))
        return s1==s2
       
        