class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p_left =0
        p_right = 0
        if len(s)==0:
            return True
        while  p_right<len(t):
            if s[p_left] == t[p_right]:
                p_left+=1
            if p_left == len(s):
                return True
            else:
                p_right +=1
        return False
        

        