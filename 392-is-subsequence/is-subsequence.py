class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p_left =0
        p_right = 0
        while p_left<len(s) and p_right<len(t):
            if s[p_left] == t[p_right]:
                p_left+=1
            p_right+=1
        
        return p_left==len(s)

        