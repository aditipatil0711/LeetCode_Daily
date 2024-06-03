class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i=0
        j=0
        m,n = len(s),len(t)

        while i < m and j<n:
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                i+=1
        return n-j
        