class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""

        for i in range(0,len(strs[0])):
            a = strs[0][i]
            for j in range(0, len(strs)):
                if  i == len(strs[j]) or strs[j][i] != a :
                    return strs[0][0:i] 
        return strs[0]
        